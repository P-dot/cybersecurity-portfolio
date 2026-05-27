# 02 — Network Services Reconnaissance Authorized

## Objetivo

Documentar conectividad, reconocimiento autorizado de servicios y análisis básico de exposición dentro de una red interna de laboratorio.

## Alcance

La práctica se realiza exclusivamente contra máquinas propias del laboratorio.

Máquinas principales:

- pfSense
- Ubuntu/vbox
- Kali Linux
- Metasploitable

## Áreas trabajadas

- Identificación de IPs actuales
- Validación de conectividad mediante `ping`
- Descubrimiento de hosts con `nmap -sn`
- Reconocimiento autorizado de servicios
- Comparación entre sistema endurecido y máquina vulnerable
- Interpretación básica de puertos y riesgos
- Recomendaciones defensivas

## Conceptos clave

- Conectividad: una máquina responde en red.
- Exposición: una máquina ofrece servicios accesibles.
- Superficie de ataque: conjunto de servicios, puertos y accesos potencialmente utilizables por un atacante.

## Hallazgos principales

- Ubuntu/vbox responde en red, pero no expone servicios visibles en los puertos principales revisados.
- Metasploitable expone múltiples servicios, como FTP, SSH, Telnet, HTTP, SMB, MySQL y VNC.
- Telnet se prioriza como riesgo alto por transmitir credenciales y comandos sin cifrado.
- SMB/445 se considera sensible por compartición de archivos, autenticación y posible movimiento lateral.
- MySQL abierto supone riesgo si acepta conexiones no restringidas.

## Recomendaciones defensivas

- Deshabilitar servicios innecesarios.
- Sustituir protocolos inseguros por alternativas cifradas.
- Restringir acceso mediante firewall.
- Limitar servicios a redes o equipos autorizados.
- Revisar logs y autenticación.
- Documentar excepciones justificadas.

## Lecciones aprendidas

- `ping` valida conectividad, pero no informa sobre servicios.
- `nmap -sn` descubre hosts activos.
- `nmap --top-ports` ayuda a revisar servicios comunes.
- No se debe analizar una IP si no está identificada dentro del alcance.
- Un operador de seguridad debe transformar puertos abiertos en riesgo, prioridad y recomendación.
