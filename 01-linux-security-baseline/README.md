# 01 — Linux Security Baseline

## Objetivo

Realizar una revisión básica de seguridad en un sistema Linux, centrada en usuarios, grupos, privilegios, permisos, servicios, puertos, firewall y logs de autenticación.

## Áreas revisadas

- Inventario inicial del sistema
- Usuario activo, grupos y privilegios sudo
- Permisos de archivos sensibles
- Revisión de directorios críticos
- Servicios activos y puertos en escucha
- Configuración básica de firewall UFW
- Revisión de sesiones y logs de sudo
- Servicios fallidos, advertencias y errores del sistema

## Hallazgos principales

- Se identificó un servicio FTP activo mediante `vsftpd`.
- Se confirmó exposición previa del puerto TCP 21.
- Se revisaron permisos sensibles en `/etc/passwd`, `/etc/shadow`, `/etc/sudoers`, `/tmp` y `.ssh`.
- Se revisaron eventos de autenticación y uso de privilegios administrativos.

## Medidas aplicadas

- Deshabilitación de `vsftpd`.
- Verificación del cierre del puerto TCP 21.
- Activación de UFW.
- Configuración de política restrictiva de entrada:
  - deny incoming
  - allow outgoing
- Revisión de logs de sesiones y eventos sudo.

## Lecciones aprendidas

- Hardening significa reducir superficie de ataque.
- Un servicio innecesario debe deshabilitarse o bloquearse.
- `ss` permite revisar puertos desde dentro del sistema.
- `journalctl`, `last`, `lastlog` y logs de sudo ayudan a reconstruir actividad relevante.
- La interpretación del contexto es clave para distinguir actividad esperada de posible anomalía.

## Competencias reforzadas

- Linux básico aplicado a seguridad
- Revisión de permisos
- Control de servicios
- Firewall básico
- Logs de autenticación
- Trazabilidad de privilegios administrativos
- Documentación técnica de evidencias
