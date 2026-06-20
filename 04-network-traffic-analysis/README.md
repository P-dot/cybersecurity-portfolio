# 04 — Network Traffic Analysis

## Overview

This lab documents a basic defensive network traffic analysis exercise performed in a controlled and authorized environment.

The objective was to capture, read, filter and interpret simple ICMP and HTTP traffic between lab systems, identifying source, destination, protocol, port, request, response and operational meaning.

No unauthorized traffic was captured and no offensive activity was performed.

## Scope

The activity was limited to an owned virtual lab environment.

Traffic was generated between lab hosts and analyzed for training purposes only.

## Tools Used

- tcpdump
- tshark
- Wireshark
- curl
- ping

## Areas Reviewed

- Capture interface identification
- ICMP traffic capture and filtering
- PCAP reading and basic interpretation
- Echo Request and Echo Reply analysis
- HTTP traffic capture
- HTTP request and response analysis
- Extraction of relevant fields with tshark
- Basic comparison between HTTP metadata and clear-text visibility

## Key Findings

- ICMP traffic confirmed basic connectivity between two lab hosts.
- HTTP traffic showed controlled client/server communication over TCP port 80.
- The HTTP capture included `HEAD` and `GET` requests.
- The server responded with `HTTP/1.1 200 OK`.
- HTTP information such as method, URI, user agent, server header and content type could be observed because the protocol was not encrypted.

## Defensive Interpretation

The lab demonstrates that network traffic analysis is not limited to confirming connectivity.

A security operator should identify who initiated the communication, the destination, the protocol, the port, the request type, the server response and whether the observed behavior is expected within the environment.

The exercise also reinforces the importance of interpreting evidence carefully: the capture confirms functional ICMP and HTTP communication, but it does not prove exploitation, credential compromise or a specific vulnerability.

## Skills Practiced

- Network traffic capture
- PCAP analysis
- ICMP interpretation
- HTTP request/response analysis
- Source and destination identification
- Protocol and port interpretation
- tshark field extraction
- Wireshark packet inspection
- Evidence-based technical documentation
- Defensive interpretation of findings

## Status

Completed.
