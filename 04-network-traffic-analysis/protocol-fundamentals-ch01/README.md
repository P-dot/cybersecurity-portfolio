# Network Protocol Fundamentals — Chapter 1

## Objective and scope

This workshop documents practical analysis of Ethernet, ARP, IPv4, ICMP, TCP, UDP and HTTP traffic in an authorized Kali Linux WSL2 lab. The goal is to demonstrate packet-level interpretation, Linux networking diagnostics and evidence-driven security operations reporting.

The workshop was informed by Chapter 1 of James Forshaw's *Attacking Network Protocols* (No Starch Press, 2017). The exercises and documentation are original; this is not a reproduction of the book.

## Environment

- Kali Linux on WSL2, Python 3, `tcpdump`, `curl` and `iproute2`.
- Local test endpoints: `127.0.0.1:8000` (HTTP) and `127.0.0.1:9999` (UDP).
- WSL2 private virtual network: `172.22.32.0/20`; example source address `172.22.42.150`, default gateway `172.22.32.1` (environment-specific; check your own routing table).
- Tools: `ip`, `ping`, `tcpdump`, `curl`, Python `socket` and `struct`.

## Network model

```text
Local TCP/UDP: Python/curl client -> loopback (lo) -> Python server
Routed ICMP: Kali eth0 -> WSL2 virtual gateway -> 1.1.1.1
Link resolution: ARP maps next-hop IPv4 addresses to link-layer MACs
Encapsulation: Ethernet -> IPv4 -> TCP / UDP / ICMP -> application data
```

The Ethernet destination for an off-subnet IPv4 packet is the next-hop gateway's MAC, not the remote destination's MAC. The IP destination remains the remote address unless modified by a device such as a NAT gateway.

## Lab 1 — Interface, routing and neighbor inspection

```bash
ip -br addr show eth0
ip route
ip route get 1.1.1.1
ip route get 127.0.0.1
ip neigh show dev eth0
```

**Observed:** Kali used its directly connected `/20` route for virtual-subnet destinations and the default gateway for external destinations. Loopback traffic used `lo`. The gateway neighbor entry was observed transitioning from `STALE` to `REACHABLE` after successful communication; `STALE` alone is not an indication of failure.

## Lab 2 — TCP handshake and HTTP payload

Terminal A:

```bash
mkdir -p ~/attacking-network-protocols/ch01
cd ~/attacking-network-protocols/ch01
printf 'Hola desde el laboratorio TCP\n' > mensaje.txt
python3 -m http.server 8000 --bind 127.0.0.1
```

Terminal B (stop with Ctrl+C **after** the request):

```bash
sudo tcpdump -i lo -nn -s 0 -w ~/attacking-network-protocols/ch01/http-local.pcap 'tcp port 8000'
```

Terminal C:

```bash
curl -v http://127.0.0.1:8000/mensaje.txt
```

Inspect after stopping the capture:

```bash
tcpdump -nn -X -r ~/attacking-network-protocols/ch01/http-local.pcap
tcpdump -nn -A -r ~/attacking-network-protocols/ch01/http-local.pcap
```

**Observed:** 12 TCP packets captured and zero kernel drops. The trace contained a SYN/SYN-ACK/ACK handshake, an 89-byte HTTP GET request, a 186-byte response-header segment, a 30-byte response body, acknowledgements and a FIN exchange. The server returned `HTTP/1.0 200 OK` to the client's HTTP/1.1 request. A FIN consumes one TCP sequence number.

### Hexadecimal IPv4/TCP interpretation

A captured HTTP request contained a 141-byte IPv4 packet:

| Component | Length |
|---|---:|
| IPv4 header | 20 bytes |
| TCP header (including timestamp options) | 32 bytes |
| HTTP request payload | 89 bytes |
| **Total IPv4 packet** | **141 bytes** |

The first IPv4 byte `0x45` encodes version 4 and an Internet Header Length of five 32-bit words (20 bytes). The IPv4 Protocol field `0x06` identifies TCP. The TCP data-offset value 8 means eight 32-bit words (32 bytes). HTTP request bytes start after both headers, with `47 45 54 20` representing `GET ` in ASCII. Header lines use CRLF (`0d 0a`).

A small standard-library verification:

```python
import struct
header = bytes.fromhex('4500008d53c040004006e8a87f0000017f000001')
version = header[0] >> 4
ihl = (header[0] & 0x0F) * 4
length = struct.unpack('!H', header[2:4])[0]
print({'version': version, 'ip_header_bytes': ihl,
       'ip_packet_bytes': length, 'protocol': header[9],
       'bytes_after_ip_header': length - ihl})
```

Expected values: version 4, IPv4 header 20 bytes, total 141 bytes, protocol 6, and 121 bytes after the IPv4 header.

## Lab 3 — UDP request and response

Terminal A, local UDP responder:

```python
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 9999))
print('UDP responder on 127.0.0.1:9999')
while True:
    data, peer = server.recvfrom(4096)
    print(peer, repr(data))
    server.sendto(b'RESPUESTA UDP: recibido', peer)
```

Terminal B:

```bash
sudo tcpdump -i lo -nn -s 0 -w ~/attacking-network-protocols/ch01/udp-local.pcap 'udp port 9999'
```

Terminal C, UDP client:

```python
import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
    client.settimeout(3)
    client.sendto(b'Hola desde UDP', ('127.0.0.1', 9999))
    print(client.recvfrom(4096))
```

Stop the capture with Ctrl+C before inspecting it:

```bash
tcpdump -nn -vv -X -r ~/attacking-network-protocols/ch01/udp-local.pcap
```

**Observed:** Two UDP datagrams, no TCP-style handshake. The request carried 14 payload bytes and a 22-byte UDP length (8-byte UDP header + 14-byte payload), inside a 42-byte IPv4 packet (20 + 8 + 14). The reply carried 23 payload bytes inside a 51-byte IPv4 packet (20 + 8 + 23). IPv4 Protocol `17` identifies UDP.

`tcpdump` reported apparent invalid UDP checksums on loopback. Checksum offload or capture-path behavior is a plausible explanation, **not a confirmed diagnosis**. The successful application exchange does not imply UDP provides reliable delivery.

## Lab 4 — ICMP, ARP and Ethernet

Start a capture on the virtual Ethernet interface:

```bash
sudo tcpdump -i eth0 -nn -e -vv -s 0 \
  -w ~/attacking-network-protocols/ch01/arp-icmp.pcap 'arp or icmp'
```

From another Kali terminal, inspect the current gateway and send limited reachability probes:

```bash
ip route
ping -c 2 -W 2 172.22.32.1  # use the gateway actually shown by ip route
ping -c 2 -W 2 1.1.1.1
ip neigh show dev eth0
```

Stop `tcpdump` with Ctrl+C, then read the capture:

```bash
tcpdump -nn -e -vv -r ~/attacking-network-protocols/ch01/arp-icmp.pcap
tcpdump -nn -e -XX -r ~/attacking-network-protocols/ch01/arp-icmp.pcap 'arp'
```

**Observed:** 12 captured packets and zero kernel drops: eight ICMP packets (two echo requests and two replies for each of the gateway and an external resolver) and four ARP packets (two requests and two replies). Each captured Ethernet ARP frame was 42 bytes: 14 bytes of Ethernet header plus 28 bytes of ARP. The capture included unicast ARP requests; ARP requests need not always be broadcast. One request contained a known target MAC, while another contained an all-zero target hardware address.

### ARP field decoding

| Field | Captured value / interpretation |
|---|---|
| Ethernet EtherType | `0x0806` = ARP |
| ARP hardware type | `0x0001` = Ethernet |
| ARP protocol type | `0x0800` = IPv4 |
| Hardware address length | `0x06` = 6 bytes |
| Protocol address length | `0x04` = 4 bytes |
| ARP operation | `0x0001` request; `0x0002` reply |
| IPv4 bytes | `ac 16 20 01` = `172.22.32.1` |
| IPv4 bytes | `ac 16 2a 96` = `172.22.42.150` |

For ICMP echo traffic, the captured IPv4 packet length was 84 bytes and the Ethernet frame length was 98 bytes. A remote echo reply had an observed TTL of 52; this does not independently establish the exact number of network hops without knowing the sender's initial TTL.

## Defensive interpretation

- Distinguish link-layer destination from network-layer destination when analyzing routed traffic.
- Decode packet fields and byte lengths rather than relying exclusively on high-level protocol labels.
- Separate observations (packet counts, field values, successful replies) from interpretations (possible checksum offload, neighbor-cache refresh).
- Treat unexpected ARP associations as items requiring corroboration, not proof of an attack by themselves.
- Recognize that cleartext HTTP payloads are visible in packet captures; use HTTPS for sensitive application data.

## Limitations and evidence handling

The work used a controlled WSL2 virtual network and localhost services. The small number of ping requests is not a network performance or reliability benchmark. No exploitation, packet injection, ARP poisoning, scanning of third-party hosts or intrusion-detection validation was performed. Raw `.pcap` files and host-specific MAC addresses remain local and are intentionally excluded from publication. Published observations were transcribed from the user's terminal outputs; raw captures were not independently retrieved or verified by the repository authoring assistant.

## Professional skills

Linux networking, IPv4 subnetting and routing, neighbor-cache interpretation, BPF capture filters, TCP/UDP socket experiments, HTTP request analysis, Ethernet/ARP/ICMP decoding, hex inspection, evidence quality and SOC/SecOps technical reporting.

## Reference

James Forshaw, *Attacking Network Protocols* (No Starch Press, 2017), Chapter 1: “The Basics of Networking.”
