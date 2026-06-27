# Cybersecurity Operations Portfolio

Portfolio técnico orientado a **ciberseguridad operativa, SOC L1, monitorización defensiva y análisis básico de evidencias**.

Este repositorio documenta laboratorios realizados en un entorno controlado y autorizado, con foco en observación, análisis, documentación técnica, tratamiento prudente de evidencias y toma de decisiones iniciales de analista.

> El objetivo no es mostrar explotación ni actividad ofensiva, sino demostrar criterio operativo defensivo: revisar sistemas, logs, tráfico, servicios y eventos, separar evidencia de interpretación y proponer acciones razonables.

---

## Perfil objetivo

Este portfolio está orientado a posiciones como:

- Operador de Seguridad
- SOC L1 / SOC Tier 1
- Técnico SOC Junior
- Técnico de Ciberseguridad Junior
- Analista de Seguridad de Infraestructura Junior
- Operador de Sistemas con orientación a seguridad
- SecOps Junior

---

## Enfoque profesional

El trabajo documentado en este repositorio sigue una lógica de operación defensiva:

- identificar fuentes de evidencia,
- revisar configuración básica de sistemas,
- observar servicios y exposición autorizada,
- analizar tráfico de red en laboratorio,
- revisar logs Linux y Windows,
- clasificar eventos por severidad y contexto,
- reducir ruido técnico,
- documentar hallazgos,
- recomendar acciones prudentes,
- escalar solo cuando la evidencia lo justifica.

---

## Laboratorios documentados

| Lab | Área | Competencias trabajadas |
|---|---|---|
| 01 — Linux Security Baseline | Sistemas Linux | Revisión básica de usuarios, permisos, servicios, logs y estado defensivo del sistema |
| 02 — Network Services Recon Authorized | Red y exposición | Identificación de activos, conectividad, servicios accesibles y superficie de exposición en entorno autorizado |
| 03 — Windows Security Baseline | Sistemas Windows | Revisión de usuarios locales, privilegios, servicios, firewall, Microsoft Defender, eventos y procesos |
| 04 — Network Traffic Analysis | Tráfico de red | Captura, filtrado e interpretación inicial de tráfico ICMP/HTTP con herramientas de terminal y Wireshark/tshark |
| 05 — Linux Log Monitoring SOC Triage | Logs Linux / SOC | Revisión de auth.log, syslog, journalctl, sudo/sesiones, servicios fallidos, severidad y acción recomendada |
| 06 — Defensive Python Log Review & SOC Reporting | Python defensivo / reporting SOC | Lectura de evidencias Linux, extracción de eventos, reducción de ruido, generación de reportes y clasificación inicial de acciones de analista |
| 07 — Windows Event Log Defensive Review | Windows logs / SOC | Revisión saneada de Security, System, Application y PowerShell logs, autenticación, errores/warnings operativos y mini triage SOC |

---

## Evidencias y documentación

Cada laboratorio prioriza documentación clara y evidencia controlada:

- README del laboratorio.
- Evidencias técnicas saneadas cuando procede.
- Separación entre datos observados, interpretación y recomendación.
- Conclusiones prudentes, sin sobredimensionar hallazgos.
- Sin credenciales, datos personales, IPs públicas sensibles ni información de terceros.

---

## Herramientas y tecnologías

- Linux
- Windows
- Windows Event Logs
- PowerShell
- Bash
- Python
- Git/GitHub
- VirtualBox
- pfSense
- Kali Linux
- Ubuntu
- Metasploitable
- Nmap autorizado
- tcpdump
- tshark
- Wireshark
- Markdown

---

## Competencias demostradas

- Monitorización básica de sistemas.
- Triaje inicial de eventos.
- Revisión de logs Linux y Windows.
- Interpretación de errores, warnings y eventos de autenticación.
- Documentación técnica orientada a SOC.
- Reporting defensivo.
- Automatización básica con Python y PowerShell.
- Análisis prudente de evidencias.
- Trabajo en entorno controlado y autorizado.
- Buenas prácticas de privacidad en evidencias públicas.

---

## Principios de trabajo

- Entorno propio, controlado y autorizado.
- Enfoque defensivo y operativo.
- No explotación de terceros.
- No publicación de datos sensibles.
- No publicación de credenciales.
- No publicación de mensajes brutos cuando puedan contener datos personales.
- Separación entre evidencia, interpretación y recomendación.
- Priorización de claridad, trazabilidad y prudencia analítica.

---

## Estado actual

Portfolio en evolución, orientado a reforzar competencias prácticas para ciberseguridad operativa y SOC L1.

Línea actual de trabajo:

1. Baseline defensivo Linux/Windows.
2. Reconocimiento autorizado de servicios.
3. Análisis básico de tráfico.
4. Monitorización y triaje de logs Linux.
5. Automatización defensiva con Python.
6. Revisión defensiva de Windows Event Logs.
7. Próximo bloque previsto: revisión de conexiones de red e indicadores básicos tipo IOC en entorno controlado.

---

## Aviso ético

Todo el contenido de este repositorio se realiza en laboratorio propio o en entornos autorizados.

Este portfolio no promueve intrusión, explotación no autorizada ni actividad ofensiva contra sistemas reales. Su finalidad es demostrar aprendizaje práctico, criterio defensivo, documentación técnica y preparación para roles de ciberseguridad operativa.



