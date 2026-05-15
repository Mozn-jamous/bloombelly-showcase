# Engineering Decisions (ADRs)

This document captures the architectural and engineering decisions made during BloomBelly's development, in the spirit of "Architecture Decision Records" (ADRs). Each entry describes the context, the decision, the alternatives we considered, and the trade-offs.

---

## ADR-001: Adopt MVVM with Provider on the Flutter Client

**Status:** Accepted
**Date:** Early design phase

### Context
We needed a state-management approach that:
- New team members could ramp up on quickly
- Supported testable view-models
- Did not impose heavy code-generation burdens
- Played well with reactive UI updates

### Decision
Use **MVVM** as the client architecture, with **Provider** for state management.

### Alternatives Considered
| Option | Why we passed |
|---|---|
| BLoC pattern | More boilerplate; steeper learning curve |
| Riverpod | Strong choice but code-gen overhead in a small team |
| MobX | Less idiomatic for Flutter as of project start |
| `setState` only | Insufficient for cross-page state sharing |

### Consequences
- Clear separation of UI from logic
- ViewModels testable in isolation
- Slightly more verbose than Riverpod, but understandable to all team members

---

## ADR-002: Python Flask Backend Instead of Supabase Edge Functions

**Status:** Accepted

### Context
We needed to orchestrate three different AI services (Gemini, LoRA-tuned transformer, Random Forest classifier) and apply server-side validation and safety filters.

### Decision
Build a **Python Flask backend** as the single point of orchestration between the mobile client and Supabase + AI providers.

### Alternatives Considered
| Option | Why we passed |
|---|---|
| Supabase Edge Functions (Deno) | Limited Python ML ecosystem; awkward for PyTorch/Transformers |
| Direct client-to-Gemini calls | Exposes API keys; no centralized safety layer |
| Node.js/Express | Python's ML libraries are vastly more mature |
| Serverless (AWS Lambda) | Cold starts unacceptable for LoRA model loading |

### Consequences
- One language across all AI orchestration (Python)
- Need to host the Flask server (more ops than pure BaaS)
- Server-side enforcement of safety pipeline, wallet rules, validation
- API keys never leave the server

---

## ADR-003: Multi-Model AI Strategy

**Status:** Accepted

### Context
A maternal health platform has three distinct AI workloads:
1. Multimodal medical image interpretation
2. Conversational Q&A on a focused medical domain
3. Stage-aware nutrition assessment

These workloads have very different requirements for accuracy, interpretability, latency, and cost.

### Decision
Use **three specialized AI components**:
- **Google Gemini** for medical image analysis
- **LoRA fine-tuned transformer** for the chatbot
- **Random Forest classifier** for nutrition evaluation

### Alternatives Considered
| Option | Why we passed |
|---|---|
| Single LLM for everything | Image understanding insufficient for medical scans; nutrition rules better suited to interpretable models |
| Full GPT-4o for all tasks | Cost and Arabic-language depth concerns |
| Build all models from scratch | Out of scope for graduation timeline |

### Consequences
- More complex orchestration but clearly bounded responsibilities
- Each component can be replaced independently
- Interpretability is preserved where it matters (nutrition)
- Costs are controllable (Gemini per-call; LoRA self-hosted; RF effectively free)

---

## ADR-004: LoRA Fine-Tuning Over Full Retraining

**Status:** Accepted

### Context
The chatbot needs domain depth in maternal/child health that out-of-the-box LLMs do not provide. Full model retraining is computationally and financially infeasible for a graduation project.

### Decision
Apply **LoRA (Low-Rank Adaptation)** to a base transformer model from Hugging Face.

### Alternatives Considered
| Option | Why we passed |
|---|---|
| RAG (Retrieval-Augmented Generation) | Considered seriously; complementary, may be added later |
| Full fine-tuning | Cost prohibitive |
| Prompt engineering only | Insufficient depth for clinical tone |
| Prefix tuning / P-tuning | Less mature ecosystem support |

### Consequences
- Lightweight model artifacts (adapters only)
- Can be served from a modest GPU/CPU
- Fast retraining when guidelines update
- Slight accuracy trade-off vs full fine-tuning

---

## ADR-005: Random Forest for Nutrition Classification

**Status:** Accepted

### Context
The nutrition evaluator must:
- Be explainable (we need to tell the user *why* a meal is or isn't suitable)
- Handle structured features (calories, macros, micronutrients)
- Be fast and offline-friendly long-term

### Decision
Use **Random Forest Classifier** (scikit-learn).

### Alternatives Considered
| Option | Why we passed |
|---|---|
| Deep neural network | Black-box; overkill for tabular data |
| Rule-based engine | Brittle to update with new guidelines |
| Logistic regression | Less accurate on non-linear nutritional thresholds |
| Gradient Boosting (XGBoost) | Slightly more accurate but heavier ops footprint |

### Consequences
- Decisions are inspectable via feature importance
- Easy to retrain when guidelines change
- Tiny model size suitable for future on-device deployment

---

## ADR-006: Doctor-Administered Account Creation

**Status:** Accepted

### Context
A health app for pregnant women must balance accessibility with safety and credibility. Anonymous self-signup creates risks (abuse, misrepresentation, no clinical oversight). On the other hand, friction in onboarding kills adoption.

### Decision
**Only doctors/clinic admins create accounts.** Users receive credentials from their healthcare provider.

### Alternatives Considered
| Option | Why we passed |
|---|---|
| Open self-registration | No clinical oversight; vulnerable to abuse |
| Hybrid (self + doctor) | Complicates the trust model |
| Invitation codes from peers | Insufficient verification |

### Consequences
- Built-in trust: every user is verified by a clinician
- Distribution requires clinic partnerships (now a feature, not a bug)
- Enables the wallet model with clinic-managed top-ups
- Adds clinical credibility for grant applications

---

## ADR-007: Wallet System Instead of In-App Payments

**Status:** Accepted (V1)

### Context
Regional payment infrastructure in Syria is constrained. International payment gateways have political and operational complications. We needed a way to monetize without depending on Stripe/PayPal.

### Decision
Use a **wallet system administered by the doctor/clinic**. Patients top up offline; usage deducts from the wallet.

### Alternatives Considered
| Option | Why we passed |
|---|---|
| Stripe/PayPal | Operationally complex in Syria |
| Local payment gateways | Adoption fragmented across the region |
| Crypto | Compliance risk; user education burden |

### Consequences
- Eliminates the regulatory and operational burden of in-app payments in V1
- Reinforces the clinic-distribution model
- Can later layer in a payment gateway as a complementary channel
- Limits direct B2C monetization until the gateway is added

---

## ADR-008: Supabase for Backend Services

**Status:** Accepted

### Context
We needed authentication, a relational database, file storage, and realtime synchronization without standing up our own infrastructure.

### Decision
Use **Supabase** for auth, Postgres, storage, and realtime.

### Alternatives Considered
| Option | Why we passed |
|---|---|
| Firebase | More mature but costs scale aggressively; NoSQL doesn't fit our relational data |
| Self-hosted Postgres + custom auth | Too much ops work for graduation timeline |
| AWS Amplify | Complex; vendor lock-in higher |

### Consequences
- Built-in Row Level Security maps cleanly to our access model
- Free tier sufficient for the pilot
- Native realtime support for wallet balance updates
- Postgres familiarity transfers to any future migration

---

## ADR-009: JWT-Based Authentication

**Status:** Accepted

### Context
We needed stateless authentication compatible with both our Flutter client and Flask backend.

### Decision
Use **JWT (JSON Web Tokens)** with short-lived access tokens and refresh tokens.

### Alternatives Considered
| Option | Why we passed |
|---|---|
| Session cookies | Stateful; requires sticky sessions |
| OAuth-only | Overkill for our user base |
| API keys | Insufficient for per-user authorization |

### Consequences
- Stateless backend (easy to scale horizontally)
- Standard tooling on both Flutter and Flask
- Token revocation requires extra design (mitigated by short expiry + refresh rotation)

---

## ADR-010: Arabic-First, Then Bilingual

**Status:** Accepted

### Context
Our target users are Arabic speakers, but English support is needed for clinical professionals and international reviewers.

### Decision
Design every flow **Arabic-first**, with English as a secondary translation layer.

### Alternatives Considered
| Option | Why we passed |
|---|---|
| English-first, Arabic translation | Inverts the actual user need |
| Arabic-only | Excludes clinical professionals |
| Auto-translate via API | Quality unacceptable for medical content |

### Consequences
- RTL layout is the default, not an afterthought
- All content is reviewed by native speakers
- English version is a faithful translation, not a rewrite
- Multi-dialect support is a roadmap item (MSA → Levantine, Gulf, Egyptian)

---

## Open Questions / Future ADRs

The following decisions are deferred to future iterations:

- **Migrating chatbot output from English to native Arabic** (model retraining needed)
- **On-device inference** for nutrition classifier and chatbot (privacy + offline support)
- **Multi-tenant data isolation** for hospital-scale deployments
- **Direct integration** with clinic EHR systems
- **HIPAA compliance pathway** if expanding to US markets
- **Federated learning** to improve models without raw data exfiltration
