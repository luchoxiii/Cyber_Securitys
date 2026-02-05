# 🟥 Security Automation Hub

Colección de **workflows automatizados** orientados a **Red Team, Blue Team, SOC, DFIR, AppSec y DevSecOps**, diseñados para ejecutarse de forma programada o bajo demanda.

El objetivo es:
- Reducir fricción operativa
- Mejorar visibilidad del attack surface
- Convertir señales técnicas en **alertas, tickets y reportes accionables**
- Facilitar ejercicios controlados y mejora continua de detección

> ⚠️ **Advertencia**  
> Varias automatizaciones están pensadas **exclusivamente para laboratorios, entornos de prueba o ejercicios con autorización explícita**.

---

## 📦 Contenido

- **A. Red Team & Pentest (30 workflows)**
- **B. Blue Team / SOC / DFIR (35 workflows)**
- **C. Application Security / DevSecOps (25 workflows)**
- **D. Platform & General Security (10 workflows)**


---

## 1. Automated Subdomain Recon Hub
**Propósito:** Consolidar inteligencia de subdominios de forma continua.  
**Integraciones:** Subfinder, Amass (Exec), DNSDB, PassiveTotal, Shodan, Censys, Slack, PostgreSQL.  
**Flujo:**  
`Cron → Exec(Subfinder/Amass) → HTTP(DNS/Passive) → HTTP(Shodan/Censys) → Merge/Unique → DB upsert → Slack summary`

---

## 2. Attack Surface Change Detector
**Propósito:** Detectar nuevos hosts, puertos o servicios respecto a la última ejecución.  
**Integraciones:** Nmap, Naabu, Masscan, Jira, Slack.  
**Flujo:**  
`Cron → Exec(scan) → Compare snapshot(DB) → Crear issues Jira por delta → Alerta Slack`

---

## 3. Cloud Bucket Finder (S3 / GCS / Azure)
**Propósito:** Enumerar buckets públicos o mal configurados.  
**Integraciones:** APIs AWS/GCP/Azure, HTTP HEAD/GET, Slack, export CSV.  
**Flujo:**  
`Cron → Listar buckets → Check ACL/URLs públicas → IF público → Slack + CSV en S3`

---

## 4. Credential Spraying Orchestrator (Lab/Test Only)
**Propósito:** Spray controlado contra IdP de laboratorio para tuning de detección.  
**Integraciones:** IdP/API custom, rate-limit, secret store.  
**Flujo:**  
`Webhook → Split lista → Delay → HTTP(Auth) → Resultados → Reporte Red/Blue`

---

## 5. GoPhish Campaign Launcher
**Propósito:** Ejecutar campañas de phishing end-to-end.  
**Integraciones:** GoPhish API, Google Sheets, Slack/Email, S3.  
**Flujo:**  
`Trigger → Targets → GoPhish(create) → Poll stats → Export CSV/PDF → Digest`

---

## 6. Malicious Macro Build Conveyor (PoC)
**Propósito:** Generar documentos PoC para laboratorios de concienciación.  
**Integraciones:** Docker builder, Git, hashing, VT sandbox privado (opcional).  
**Flujo:**  
`Webhook → Build(Docker) → Hash → S3 → Link + Slack`

---

## 7. Payload Inventory & Hash Tracker
**Propósito:** Inventario de artefactos, hashes y uso.  
**Integraciones:** S3, PostgreSQL, Slack.  
**Flujo:**  
`Upload → SHA256 → DB upsert(who/when/use) → Slack`

---

## 8. C2 Beacon Event Forwarder
**Propósito:** Enviar eventos C2 a canales colaborativos.  
**Integraciones:** CS / Havoc / Sliver, Slack/Discord, TimescaleDB.  
**Flujo:**  
`Webhook(C2) → Transform → DB → Slack por host`

---

## 9. Initial Access Monitor (Decoy Links)
**Propósito:** Observar clicks, IPs y User-Agents.  
**Integraciones:** Webhook, GeoIP, AbuseIPDB.  
**Flujo:**  
`Click → Enrich → IF mala reputación → IOC → TI DB`

---

## 10. Exfiltration Simulation to Cloud
**Propósito:** Probar detección DLP.  
**Integraciones:** S3, GDrive, Dropbox, Slack.  
**Flujo:**  
`Cron → Upload decoy → Verify → Notify SOC`

---

## 11. AV/EDR Evasion Test Matrix Runner (Lab)
**Propósito:** Ejecutar variaciones OPSEC contra EDR de laboratorio.  
**Integraciones:** Exec, Git samples, Jira.  
**Flujo:**  
`Schedule → Execute → Collect detections → Jira para misses`

---

## 12. TLS / Cert Recon Harvester
**Propósito:** Seguimiento de emisión de certificados y SANs.  
**Integraciones:** crt.sh, Censys, DB, Email.  
**Flujo:**  
`Cron → Query → Diff histórico → Email cambios`

---

## 13. Shadow IT Finder
**Propósito:** Identificar dominios y apps no gestionados.  
**Integraciones:** SecurityTrails, Shodan, HTTP banners.  
**Flujo:**  
`Fetch → HTTP checks → Tag sospechosos → Reporte`

---

## 14. Vuln Exploit Window Notifier
**Propósito:** Alertar cuando aparece un PoC para CVEs in-scope.  
**Integraciones:** GitHub RSS, NVD, Exploit-DB, Slack.  
**Flujo:**  
`Poll feeds → Match CVEs → Slack alert`

---

## 15. Password Dump Honeytoken Telemetry
**Propósito:** Detectar reutilización de credenciales.  
**Integraciones:** Canarytokens, Webhook, TI DB.  
**Flujo:**  
`Fire → Enrich → Store IOC → Notify`

---

## 16. Adversary Path Builder (ATT&CK)
**Propósito:** Construir rutas ordenadas de técnicas.  
**Integraciones:** JSON, Exec scripts, Confluence.  
**Flujo:**  
`Select perfil → Iterate técnicas → Logs → Runbook`

---

## 17. Browser Exploit Canary (XSS)
**Propósito:** Recibir callbacks de payloads inyectados.  
**Integraciones:** Webhook, Slack, urlscan.io.  
**Flujo:**  
`Payload → Fire → Evidencia + Slack`

---

## 18. SSRF Canary Endpoint
**Propósito:** Detectar intentos SSRF.  
**Integraciones:** Webhook, GeoIP, parser de headers.  
**Flujo:**  
`Hit → Parse → Map app → Reporte`

---

## 19. Perimeter Tech Stack Mapper
**Propósito:** Fingerprinting tecnológico a escala.  
**Integraciones:** WhatWeb / Wappalyzer, DB.  
**Flujo:**  
`Enumerate → Fingerprint → Store/Trend`

---

## 20. Default Creds Sweep (Lab)
**Propósito:** Validar controles contra credenciales débiles.  
**Integraciones:** HTTP, SSH, SNMP, Slack.  
**Flujo:**  
`Lista → Paralelo → Resultados → Slack`

---

## 21. API Fuzzing Loop (Dev/Test)
**Propósito:** Fuzzing nocturno de APIs.  
**Integraciones:** ZAP, ffuf, Katana, Jira.  
**Flujo:**  
`Cron → Discover → Fuzz → Dedup → Jira`

---

## 22. Email Security Bypass Lab
**Propósito:** Probar controles de correo (EOP / GWS).  
**Integraciones:** SMTP, IMAP/Gmail API, VirusTotal.  
**Flujo:**  
`Send → Verdicts → Score → Reporte`

---

## 23. Windows Lateral Movement Lab Runner
**Propósito:** Practicar PSRemoting, WMI y SMB.  
**Integraciones:** WinRM, SSH jump host, Logging DB.  
**Flujo:**  
`Tasks → Execute → Capture → Heatmap`

---

## 24. Phishing Landing Page Telemetry
**Propósito:** Telemetría detallada de usuarios.  
**Integraciones:** Webhook, device fingerprint, GeoIP.  
**Flujo:**  
`Capture → Normalize → Risk score → CSV`

---

## 25. Recon to Report (One‑Click)
**Propósito:** Generar reportes PDF de recon.  
**Integraciones:** DB, Markdown, PDF, Confluence.  
**Flujo:**  
`Query → Render → Convert → Publish`

---

## 26. Bluetooth / IoT Discovery (Lab)
**Propósito:** Detectar BLE e IoT rogue.  
**Integraciones:** Sensor API, DB, Slack.  
**Flujo:**  
`Poll → New MACs → Alert`

---

## 27. WiFi Evil Twin Drill Tracker
**Propósito:** Simular y registrar detecciones WiFi.  
**Integraciones:** hostapd, airmon-ng, Slack.  
**Flujo:**  
`Run → Log → Timeline`

---

## 28. Red Team Debrief Packager
**Propósito:** Empaquetar artefactos y timelines.  
**Integraciones:** S3, ZIP, Confluence, Jira.  
**Flujo:**  
`Select → Pull → Zip → Upload`

---

## 29. OpSec Sanity Checker
**Propósito:** Validar higiene de infraestructura antes de operaciones.  
**Integraciones:** DNS, WHOIS, CDN, IP reputation, Cloud SG.  
**Flujo:**  
`Validate → IF leak → Blocker alert`

---

## 30. C2 Infra Expiry & Burn Plan
**Propósito:** Retirar infraestructura automáticamente.  
**Integraciones:** Cloud APIs, DNS API, Slack.  
**Flujo:**  
`Daily check → TTL reached → Destroy → Log`

# B. Blue Team / SOC / DFIR (35)

---

## 31. Threat Intel Ingest & Normalize
**Propósito:** Agregar y normalizar feeds TI (OTX, MISP, VT, AbuseIPDB).  
**Integraciones:** HTTP, CSV/JSON, PostgreSQL, Elastic.  
**Flujo:**  
`Cron → Fetch feeds → Map fields (STIX-ish) → Upsert → Métricas de de-dup`

---

## 32. IOC Enrichment Micro-SOAR
**Propósito:** Enriquecimiento bajo demanda de IPs, URLs y hashes.  
**Integraciones:** VirusTotal, urlscan.io, WHOIS, Shodan.  
**Flujo:**  
`Webhook IOC → Enrich paralelo → Score confianza → Respuesta JSON`

---

## 33. Impossible Travel Detector
**Propósito:** Detectar anomalías geográficas en accesos IdP.  
**Integraciones:** Okta, Azure AD, GeoIP, Slack, Jira.  
**Flujo:**  
`Pull eventos → Agrupar por usuario → Cálculo velocidad → Alerta`

---

## 34. OAuth App Risk Auditor
**Propósito:** Detectar grants OAuth de alto riesgo.  
**Integraciones:** Google Workspace, M365 Graph, Sheets, Slack.  
**Flujo:**  
`Pull grants → Score scopes → Notificar owners`

---

## 35. SIEM → Slack Alert Router
**Propósito:** Alertas dirigidas y deduplicadas.  
**Integraciones:** Splunk, Elastic API, Slack threads.  
**Flujo:**  
`Poll alerts → IF severidad+no visto → Thread por incidente`

---

## 36. EDR Noise Tamer
**Propósito:** Suprimir falsos positivos conocidos.  
**Integraciones:** CrowdStrike, Defender API, Redis.  
**Flujo:**  
`Ingest → Check allowlist → IF nuevo → Escalar`

---

## 37. Phishing Auto‑Triage
**Propósito:** Clasificar, detonar y dictaminar phishing.  
**Integraciones:** Gmail / Graph, VT, AnyRun, Jira.  
**Flujo:**  
`Fetch reportes → Extraer IOCs → Sandbox → Verdict → Ticket`

---

## 38. Ransomware Canary Tripwire
**Propósito:** Detección temprana de cifrado.  
**Integraciones:** SMB watcher, Slack, runbook IR.  
**Flujo:**  
`Monitor canary → IF spike entropía → Page on‑call`

---

## 39. DNS Tunneling Heuristics
**Propósito:** Detectar queries largos/frecuentes.  
**Integraciones:** Logs DNS (Elastic), scoring function.  
**Flujo:**  
`Job diario → Flag FQDNs → Cross‑check TI → Alerta`

---

## 40. Beaconing Periodicity Detector
**Propósito:** Detectar intervalos tipo C2.  
**Integraciones:** Proxy / NetFlow, FFT.  
**Flujo:**  
`Pull flows → Periodograma → Alertar candidatos`

---

## 41. URL Detonation Pipeline
**Propósito:** Clasificar URLs de alertas.  
**Integraciones:** urlscan.io, VT, Screenshot API, S3.  
**Flujo:**  
`Scan → Screenshot → Store → Verdict`

---

## 42. Abuse Mailbox Automation
**Propósito:** Triage automático de spam reportado.  
**Integraciones:** IMAP, Regex, Jira.  
**Flujo:**  
`Leer inbox → Extraer IOCs → Enrich → Cerrar o escalar`

---

## 43. Threat Actor Tracker
**Propósito:** Seguimiento de infraestructura APT.  
**Integraciones:** Feeds TI, ASN/IP WHOIS.  
**Flujo:**  
`Monitor actores → Update watchlists → Digest`

---

## 44. SOAR Containment Buttons
**Propósito:** Acciones de contención semi‑automáticas.  
**Integraciones:** EDR, FW/WAF, Okta.  
**Flujo:**  
`Slack action → Webhook → Ejecutar API → Confirmar`

---

## 45. Cloud Config Drift Watch
**Propósito:** Detectar cambios riesgosos en cloud.  
**Integraciones:** AWS, GCP, Azure config APIs, Jira.  
**Flujo:**  
`Diff horario → IF público/escalación → Ticket`

---

## 46. S3 Public Object Sentinel
**Propósito:** Alertar ACLs públicas.  
**Integraciones:** AWS S3, Slack.  
**Flujo:**  
`ListObjects → Check ACL → Alert + fix sugerido`

---

## 47. Exposed Secret Honeypot
**Propósito:** Detectar leaks de secretos.  
**Integraciones:** Canarytokens, TI DB.  
**Flujo:**  
`Trigger → Enrich → Update blocklists`

---

## 48. Endpoint Tamper Watch
**Propósito:** Detectar intentos de deshabilitar EDR.  
**Integraciones:** Eventos EDR, Slack paging.  
**Flujo:**  
`Subscribe → IF tamper → Page + incidente`

---

## 49. Macro Risk Scorer
**Propósito:** Puntuar riesgo en adjuntos Office.  
**Integraciones:** O365, Google, OLE parser, VT.  
**Flujo:**  
`Download → Analyze → Score → Verdict`

---

## 50. Okta MFA Fatigue Monitor
**Propósito:** Detectar spam de MFA.  
**Integraciones:** Okta logs, Slack, Jira.  
**Flujo:**  
`Count prompts → IF anómalo → Alertar`

---

## 51. Brute‑Force Heatmap
**Propósito:** Visualizar fallos de autenticación.  
**Integraciones:** SIEM, Grafana / Looker.  
**Flujo:**  
`Extract diario → Aggregate → Dashboard`

---

## 52. Insider Data Egress Guard
**Propósito:** Detectar picos de exfiltración interna.  
**Integraciones:** DLP logs, Drive / OneDrive APIs.  
**Flujo:**  
`Pull eventos → Threshold → Escalar`

---

## 53. Malspam Campaign Correlator
**Propósito:** Agrupar campañas de malspam.  
**Integraciones:** IMAP, certs TLS, IP origen.  
**Flujo:**  
`Cluster features → Label → Reporte`

---

## 54. IR War Room Orchestrator
**Propósito:** Crear war room de incidentes.  
**Integraciones:** Slack / Teams, Confluence, PagerDuty.  
**Flujo:**  
`Webhook → Canal → Runbook → Page roles`

---

## 55. Asset Risk Joiner
**Propósito:** Correlacionar CMDB + vuln + EDR.  
**Integraciones:** ServiceNow, Qualys/Tenable, EDR.  
**Flujo:**  
`Join nocturno → Ownership → Top 10 riesgos`

---

## 56. Threat Hunt Notebook Seeds
**Propósito:** Empujar IOCs a hunting.  
**Integraciones:** Searches guardadas, Jupyter.  
**Flujo:**  
`Cambio TI → Queries → SOC channel`

---

## 57. GeoIP Block Auto‑Update
**Propósito:** Mantener bloqueos geográficos actualizados.  
**Integraciones:** Firewall API, GeoIP DB.  
**Flujo:**  
`Refresh mensual → Apply → Verify`

---

## 58. Password Leak Monitor
**Propósito:** Monitor de credenciales comprometidas.  
**Integraciones:** HaveIBeenPwned (k‑Anon), HR DB, Email.  
**Flujo:**  
`Search hash → IF match → Notify + reset`

---

## 59. Public Paste Scraper
**Propósito:** Detectar leaks en pastes/repos públicos.  
**Integraciones:** Pastebin, GitHub search, Regex, Jira.  
**Flujo:**  
`Crawl → Extract → De‑dupe → Tickets`

---

## 60. SOC Daily Briefing Builder
**Propósito:** Digest diario del SOC.  
**Integraciones:** SIEM, TI deltas, Incidentes abiertos.  
**Flujo:**  
`07:30 Cron → Compile → Email / Slack`

---

## 61. Endpoint Golden Image Drift
**Propósito:** Detectar drift del baseline.  
**Integraciones:** EDR inventory, hashes.  
**Flujo:**  
`Compare semanal → Deviaciones → Fix tasks`

---

## 62. VPN Anomaly Detector
**Propósito:** Detectar sesiones VPN anómalas.  
**Integraciones:** Logs VPN, Function.  
**Flujo:**  
`Aggregate → Z‑score → Alertar`

---

## 63. Shadow Admin Finder
**Propósito:** Detectar cuentas privilegiadas ocultas.  
**Integraciones:** AD, Azure AD, IAM APIs.  
**Flujo:**  
`Enumerate roles → Diff → Notify`

---

## 64. Email Auth Health (SPF / DKIM / DMARC)
**Propósito:** Prevenir spoofing.  
**Integraciones:** DNS checks, parser DMARC.  
**Flujo:**  
`Check semanal → Score → Acciones`

---

## 65. Webhook Abuse Sentinel
**Propósito:** Detectar abuso de webhooks.  
**Integraciones:** API gateways, métricas rate.  
**Flujo:**  
`Monitor → Threshold → Block rule`

---

## 66. Printer / OT Device Watch
**Propósito:** Anomalías OT y dispositivos legacy.  
**Integraciones:** Syslog, NetFlow, OT vendor API.  
**Flujo:**  
`Collect → Rules → Notify OT`

---

## 67. SSL / TLS Weak Cipher Patrol
**Propósito:** Detectar cifrados débiles.  
**Integraciones:** sslscan, sslyze, DB.  
**Flujo:**  
`Scan → Parse → Jira tasks`

---

# C. Application Security / DevSecOps (25)

---

## 68. SAST on PR with Semgrep
**Propósito:** Análisis estático en PR.  
**Integraciones:** GitHub/GitLab, Semgrep (Docker), Jira.  
**Flujo:**  
`Webhook PR → Run Semgrep → Annotate checks → Fail/Pass → Ticket`

---

## 69. DAST Nightly with ZAP
**Propósito:** Crawl/scan staging.  
**Integraciones:** ZAP API, Slack, HTML report → S3.  
**Flujo:**  
`Cron → ZAP Spider+Active → Threshold → Notify`

---

## 70. Software Composition Analysis
**Propósito:** Detectar vulnerabilidades en dependencias.  
**Integraciones:** Trivy/Grype, GH Dependabot API.  
**Flujo:**  
`Build event → Scan → SBOM → Gate release`

---

## 71. Container Image Policy Gate
**Propósito:** Bloquear imágenes con CVEs críticos.  
**Integraciones:** Trivy, Registry API, ArgoCD.  
**Flujo:**  
`Push → Scan → IF critical → Block tag → Notify`

---

## 72. IaC Misconfig Scanner
**Propósito:** Validar Terraform/K8s.  
**Integraciones:** Checkov/Terraform Cloud, Jira.  
**Flujo:**  
`PR → Scan → Inline findings → Ticket`

---

## 73. Secrets Scanner
**Propósito:** Prevenir leaks de claves.  
**Integraciones:** TruffleHog/Gitleaks, Slack.  
**Flujo:**  
`Commit hook → Scan → Quarantine → Rotate reminder`

---

## 74. CICD SBOM + Provenance
**Propósito:** Attestations tipo SLSA.  
**Integraciones:** Syft, Cosign, Registry.  
**Flujo:**  
`Build → SBOM → Sign → Attach artifact`

---

## 75. API Contract Drift Guard
**Propósito:** Alertar sobre drift OpenAPI.  
**Integraciones:** SwaggerHub/Postman, ZAP passive.  
**Flujo:**  
`PR → Diff OpenAPI → Raise change approvals`

---

## 76. GraphQL Introspection Guard
**Propósito:** Bloquear introspección en prod.  
**Integraciones:** HTTP check, WAF.  
**Flujo:**  
`Check diario → IF enabled → Ticket → Push WAF fix`

---

## 77. CSP/Headers Compliance
**Propósito:** Validar headers de seguridad.  
**Integraciones:** HTTP HEAD, Report-Only evaluation.  
**Flujo:**  
`Crawl → Evaluate → Gap report`

---

## 78. File Upload Abuse Tests
**Propósito:** Probar bypass MIME/polyglot.  
**Integraciones:** ZAP / scripts custom, S3.  
**Flujo:**  
`Test set → Upload → Analyze response → Raise bugs`

---

## 79. SSRF Canary Test Pack
**Propósito:** Validar filtros de egress.  
**Integraciones:** Canary endpoint, logs.  
**Flujo:**  
`Send crafted URLs → Check callbacks → Report`

---

## 80. Rate Limit & AuthZ Fuzzer
**Propósito:** Detectar flaws de business logic.  
**Integraciones:** Ffuf / Katana, test users.  
**Flujo:**  
`Scenario runner → Detect 429/401 gaps → Ticket`

---

## 81. Mobile AppSec via MobSF
**Propósito:** Escanear APK / IPA.  
**Integraciones:** MobSF API, Slack.  
**Flujo:**  
`Upload build → Scan → Risk grade → Gate release`

---

## 82. Dependency Auto-PR Remediator
**Propósito:** Auto-bump libs.  
**Integraciones:** Renovate/Bot, CI.  
**Flujo:**  
`Nightly → Raise PRs → Tag owners → Merge if green`

---

## 83. Static Secrets Rotation Helper
**Propósito:** Track key ages.  
**Integraciones:** Vault / Secrets Manager, Git.  
**Flujo:**  
`Inventory → Age calc → Reminders`

---

## 84. App Attack Telemetry Loop
**Propósito:** Replay de ataques prod en staging.  
**Integraciones:** WAF logs, ZAP replay.  
**Flujo:**  
`Extract patterns → Generate cases → Scan staging`

---

## 85. Compliance Pack (PCI/SOC2)
**Propósito:** Evidencia de controles.  
**Integraciones:** Cloud APIs, CI logs, Jira.  
**Flujo:**  
`Monthly pull → Bundle → Confluence`

---

## 86. Feature-Flag Abuse Tests
**Propósito:** Control de flags.  
**Integraciones:** FF platform API, test scripts.  
**Flujo:**  
`Enumerate → Cross-role test → Report`

---

## 87. CORS / Redirect Weakness Finder
**Propósito:** Detectar combos inseguros.  
**Integraciones:** HTTP checks, regex.  
**Flujo:**  
`Crawl → Test origins → Flag dangerous combos`

---

## 88. Session Management Validations
**Propósito:** Validar cookies / rotation.  
**Integraciones:** HTTP, ZAP scripts.  
**Flujo:**  
`Login → Action → Invalidate → Verify`

---

## 89. CI Artifact Leakage Guard
**Propósito:** Detectar exposición de artifacts privados.  
**Integraciones:** CI API, Bucket scans.  
**Flujo:**  
`Enumerate → Try fetch → Ticket`

---

## 90. Access Tokens Exposure Watch
**Propósito:** Detectar tokens públicos.  
**Integraciones:** GH/GitLab search, regex.  
**Flujo:**  
`Search org → Alert → Revoke / rotate tasks`

---

## 91. SCA License Compliance
**Propósito:** Validar cumplimiento de licencias.  
**Integraciones:** FOSSology / Trivy, Jira.  
**Flujo:**  
`Analyze SBOM → Violations → Tickets`

---

## 92. Perf & Sec Regression Join
**Propósito:** Correlacionar performance + sec.  
**Integraciones:** k6/Gatling, ZAP.  
**Flujo:**  
`Run → Correlate regressions → Gate release`

---

# D. Platform & General Security (10)

---

## 93. Vuln Digest with Prioritization
**Propósito:** CVEs → exposición → exploitability.  
**Integraciones:** NVD, EPSS/KEV, CMDB, Jira.  
**Flujo:**  
`Fetch CVEs → Join assets → Score → Ticket`

---

## 94. TLS Expiry & Rotation Planner
**Propósito:** Evitar expiraciones sorpresa.  
**Integraciones:** crt.sh, Cert managers, Calendar.  
**Flujo:**  
`Gather expiring → Plan → Email owners`

---

## 95. Risk Register Auto-Curator
**Propósito:** Mantener riesgos actualizados.  
**Integraciones:** Jira / ServiceNow, Sheets.  
**Flujo:**  
`Weekly sync → Archive stale → Nudge owners`

---

## 96. Backup Integrity & RPO Check
**Propósito:** Validar SLAs de backup.  
**Integraciones:** Backup API, Hashing, Slack.  
**Flujo:**  
`Verify jobs → Sample restore → Report`

---

## 97. Data Classification Guardrails
**Propósito:** Etiquetado de datos y control de propagación.  
**Integraciones:** DLP, Drive / SharePoint APIs.  
**Flujo:**  
`Scan labels → IF sensitive public → Auto-restrict`

---

## 98. Geo Blocklist Lifecycle
**Propósito:** Mantener política geográfica.  
**Integraciones:** GeoIP, FW APIs.  
**Flujo:**  
`Quarterly review → Update rules → Verify reachability`

---

## 99. Security Awareness Insights
**Propósito:** KPI de formación vs incidentes.  
**Integraciones:** LMS, SIEM, BI.  
**Flujo:**  
`Join datasets → KPI report → Exec summary`

---

## 100. Red↔Blue Exercise Loop (Purple)
**Propósito:** Simular, detectar y mejorar controles.  
**Integraciones:** ATT&CK set, ZAP / Caldera / Atomic, SIEM / EDR.  
**Flujo:**  
`Plan técnicas → Execute → Collect detections → Engineering tasks`

---


---

## 🛡️ Uso Responsable

Este repositorio está diseñado para:
- Red Team autorizado
- Laboratorios y simulaciones
- Purple Team
- Mejora de detección y respuesta

❌ **No utilizar en entornos productivos ni contra activos sin permiso explícito.**

---



## 📄 Licencia
Uso interno / educativo. Adaptar según políticas de la organización.
