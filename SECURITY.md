# Security Policy

BloomBelly handles sensitive health information about mothers, children, and families. We take security seriously and treat reported vulnerabilities as high priority.

## Supported Versions

| Version | Status | Security Updates |
|---|---|---|
| 1.x (MVP — graduation submission) | Active | ✅ Yes |
| Pre-release | Deprecated | ❌ No |

## Reporting a Vulnerability

If you discover a security vulnerability in BloomBelly, please **do not open a public GitHub issue.**

Instead, report it privately by emailing:

📧 **moznjamous9@gmail.com**

Subject line: `[SECURITY] BloomBelly — Brief description`

Include:
- A clear description of the issue and its potential impact
- Steps to reproduce
- Any proof-of-concept code or screenshots (please redact PII)
- Your contact information for follow-up

### What to Expect

| Action | Target Timeline |
|---|---|
| Acknowledgement of receipt | Within 48 hours |
| Initial assessment | Within 5 business days |
| Fix timeline (depending on severity) | Critical: 7 days · High: 14 days · Medium: 30 days |
| Public disclosure | Coordinated with the reporter, typically after a fix is shipped |

We will credit you in the resolution announcement unless you prefer to remain anonymous.

## Security Practices

The following practices are built into BloomBelly:

### Authentication & Authorization
- **JWT tokens** with short expiration and refresh-token rotation
- **bcrypt password hashing** with a minimum work factor of 12
- **Doctor-administered account creation** — no anonymous signups
- **Token storage** in platform-secured keychains (`flutter_secure_storage`)

### Database
- **Row-Level Security (RLS)** policies on every table, scoped to `auth.uid()`
- **No raw SQL** from client; all writes go through validated endpoints
- **Cascade deletes** for GDPR right-to-erasure compliance
- **Daily backups** with point-in-time recovery

### API & Network
- **HTTPS only** — no plain HTTP endpoints
- **Input validation** on all server endpoints (Flask)
- **Rate limiting** on authentication and AI-inference endpoints
- **No API keys** in client builds — all model calls proxied through Flask

### AI & Privacy
- **PII stripping** before forwarding any data to external AI APIs
- **Image redaction** when needed before Gemini analysis
- **Chat-log review** policy: chats are stored locally for user reference but not used as training data without explicit consent
- **Medical disclaimers** on every AI-generated response

### Mobile Client
- **No sensitive data in shared_preferences** — sensitive items go to secure storage
- **Certificate pinning** (planned for production release)
- **Obfuscation** of release builds (Dart `--obfuscate`)

## Out of Scope

The following are explicitly **not** in scope for security reports:

- Issues requiring physical access to an unlocked device
- Social-engineering attacks against the clinic/admin staff
- Denial of service caused by extreme call volume to free-tier services
- Vulnerabilities in upstream open-source dependencies (please report those to the upstream maintainers)
- Findings already documented in this file

## Past Disclosures

No security advisories at this time.

## Compliance Roadmap

We are tracking the following compliance frameworks for future production releases:

- **GDPR** (EU) — right to access, portability, erasure
- **PDPL** (Saudi Arabia) — personal data protection
- **HIPAA** (US) — if we expand into US markets (requires Supabase BAA)
- **WHO Digital Health Ethics Guidelines**

Current status: not yet certified for any of the above; design choices are oriented toward future compliance.
