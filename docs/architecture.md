# BloomBelly — System Architecture

This document describes the actual technical architecture of BloomBelly as implemented for our graduation project at Al-Sham Private University.

## Table of Contents
- [Architectural Style](#architectural-style)
- [Client Architecture (MVVM)](#client-architecture-mvvm)
- [Backend (Python Flask)](#backend-python-flask)
- [AI / ML Pipeline](#ai--ml-pipeline)
- [Data Layer (Supabase)](#data-layer-supabase)
- [Sequence: Login Flow](#sequence-login-flow)
- [Sequence: Medical Test Analysis](#sequence-medical-test-analysis)
- [Sequence: Wallet & Paid Services](#sequence-wallet--paid-services)
- [Security & Privacy](#security--privacy)

---

## Architectural Style

BloomBelly follows the **MVVM (Model-View-ViewModel)** pattern on the client, paired with a **Python Flask** backend that orchestrates AI services and database operations.

```mermaid
flowchart LR
    UI[Flutter UI<br/>View] --> VM[ViewModel<br/>Provider]
    VM --> M[Model]
    M -->|REST| FLASK[Flask API]
    FLASK --> AI[AI Services]
    FLASK --> SUPA[(Supabase)]
```

**Why MVVM?**
- Clean separation between presentation and logic
- Testable ViewModels independent of UI
- Provider gives reactive state with minimal boilerplate

**Why Flask backend?**
- Orchestrates multiple AI services (Gemini, LoRA-tuned model, Random Forest)
- Hides API keys and model weights from the client
- Centralizes business logic and validation

---

## Client Architecture (MVVM)

```mermaid
graph TB
    subgraph V[View — Pages & Widgets]
        HOME[Home Page]
        TRACK[Pregnancy Tracker]
        KICK[Kick Counter]
        TEST[Test Analyzer]
        CHAT[AI Chat]
        WALLET[Wallet]
        SETTINGS[Settings]
    end

    subgraph VM[ViewModel Layer]
        AUTH_VM[AuthViewModel]
        PREG_VM[PregnancyViewModel]
        KICK_VM[KickCounterViewModel]
        TEST_VM[TestAnalyzerViewModel]
        CHAT_VM[ChatViewModel]
        WALLET_VM[WalletViewModel]
    end

    subgraph M[Model Layer]
        USER_M[User Model]
        PREG_M[Pregnancy Model]
        TEST_M[Test Result Model]
        TRANS_M[Transaction Model]
    end

    HOME --> AUTH_VM
    TRACK --> PREG_VM
    KICK --> KICK_VM
    TEST --> TEST_VM
    CHAT --> CHAT_VM
    WALLET --> WALLET_VM

    AUTH_VM --> USER_M
    PREG_VM --> PREG_M
    TEST_VM --> TEST_M
    WALLET_VM --> TRANS_M
```

State management uses **Provider** with reactive notifiers. All API calls are routed through repository classes that handle errors and caching.

---

## Backend (Python Flask)

The Flask backend exposes RESTful APIs and orchestrates three AI services:

```mermaid
graph TB
    subgraph Flask["Python Flask Backend"]
        ROUTES[REST Routes]
        AUTH_MW[JWT Auth Middleware]
        VALID[Input Validation]
        ORCH[AI Orchestrator]
        REPO[Data Repositories]
    end

    subgraph Endpoints[Key Endpoints]
        E1[POST /auth/login]
        E2[POST /tests/analyze]
        E3[POST /chat/message]
        E4[POST /nutrition/evaluate]
        E5[GET /wallet/balance]
        E6[POST /wallet/subscribe]
    end

    ROUTES --> AUTH_MW
    AUTH_MW --> VALID
    VALID --> ORCH
    VALID --> REPO

    E1 --> ROUTES
    E2 --> ROUTES
    E3 --> ROUTES
    E4 --> ROUTES
    E5 --> ROUTES
    E6 --> ROUTES
```

**Key responsibilities:**
- JWT token issuance & verification
- Image preprocessing before forwarding to Gemini
- Prompt assembly & post-processing for the chatbot
- Feature engineering for the nutrition classifier
- Wallet balance checks before paid-service usage

---

## AI / ML Pipeline

BloomBelly integrates **three distinct AI components**, each tuned for its specific job:

### 1. Medical Image Analysis (Google Gemini)

```mermaid
sequenceDiagram
    participant U as User
    participant App as Flutter App
    participant Flask as Flask Backend
    participant Storage as Supabase Storage
    participant Gemini as Gemini API
    participant DB as Supabase DB

    U->>App: Uploads lab/ultrasound image
    App->>Storage: Upload image
    Storage-->>App: Image URL
    App->>Flask: POST /tests/analyze {url, type}
    Flask->>Storage: Fetch image
    Flask->>Gemini: Analyze (prompt + image)
    Gemini-->>Flask: Plain-language summary
    Flask->>DB: Save result + timestamp
    Flask-->>App: Simplified explanation
    App-->>U: Display friendly result
```

### 2. Fine-Tuned Medical Chatbot (LoRA + Transformers)

```mermaid
flowchart TB
    Q[Arabic question from user] --> TRANS[Translation to English]
    TRANS --> CHECK{Within scope?}
    CHECK -->|Maternal/child health| MODEL[LoRA fine-tuned model<br/>via Hugging Face Transformers]
    CHECK -->|Out of scope| REJ[Polite rejection]
    MODEL --> SAFETY[Safety + citation layer]
    SAFETY --> ENG[English response]
    ENG --> USER[Display to user]
```

**Why LoRA?** Lightweight fine-tuning of a base transformer keeps the model small enough to run on a modest server while specializing it for pregnancy, nutrition, and pediatric topics.

### 3. Nutrition Classifier (Random Forest)

```mermaid
flowchart LR
    INPUT[User enters meal data<br/>calories, protein, iron, ...] --> FE[Feature engineering]
    FE --> RF[Random Forest Classifier]
    RF --> RESULT{Result}
    RESULT -->|Suitable| GREEN[✅ Suitable for stage]
    RESULT -->|Not suitable| RED[⚠️ Adjustment suggested]
    GREEN --> SAVE[Save to nutrition log]
    RED --> SUGG[Show alternatives]
```

Trained on pregnancy-stage nutritional requirements, with features like calorie content, protein, iron, folic acid, and calcium.

---

## Data Layer (Supabase)

Supabase provides four services we use:

| Service | Purpose |
|---|---|
| **PostgreSQL** | All persistent data (users, pregnancies, kicks, tests, wallet) |
| **Auth** | Account management (created by Manager role) |
| **Storage** | Medical test images, profile photos |
| **Realtime** | Live wallet balance updates, multi-device sync |

### Key Tables (from ERD)

- `users` — base user account
- `manager` — admin/doctor entries
- `pregnancies` — pregnancy timeline
- `children` — child profiles for second-time mothers
- `fetal_moves` — kick counter entries
- `pregnancy_weight` — weight tracking
- `weekly_templates` — week-specific content
- `nutrition` — meal entries with classifier results
- `medical_tests` — uploaded tests + AI analysis
- `vaccine` — vaccination records
- `sleep_test` — child sleep entries
- `growth` — child growth measurements (WHO standards)
- `wallet_tx` — wallet transactions
- `transaction` — paid-service usage log
- `care_guides` — first-aid content
- `suggestions` — week-based pregnancy guidance

All sensitive tables have **Row Level Security** policies scoped to `auth.uid()`.

---

## Sequence: Login Flow

```mermaid
sequenceDiagram
    participant U as User
    participant V as Mobile UI
    participant Auth as Auth Service
    participant DB as Users Table

    U->>V: Enter email + password
    V->>Auth: POST /login
    Auth->>DB: SELECT user WHERE email
    alt Password matches
        DB-->>Auth: User row
        Auth-->>V: 200 OK + JWT
        V-->>U: Navigate to home
    else Wrong password
        Auth-->>V: 401 Unauthorized
        V-->>U: Show "Invalid credentials"
        V->>U: Offer "Forgot password" link
    end
```

---

## Sequence: Medical Test Analysis

```mermaid
sequenceDiagram
    participant U as User
    participant App as Flutter
    participant FS as Flask
    participant Gem as Gemini API
    participant DB as Supabase

    U->>App: Take photo of lab result
    App->>FS: Upload image + metadata
    FS->>DB: Store image reference
    FS->>Gem: Send image + analysis prompt
    Gem-->>FS: Structured findings
    FS->>DB: Persist analysis + timestamp
    FS-->>App: Plain-language summary
    App-->>U: Show findings + recommended follow-up
```

---

## Sequence: Wallet & Paid Services

```mermaid
sequenceDiagram
    participant U as User
    participant App as Flutter
    participant FS as Flask
    participant DB as Wallet Table

    U->>App: Tap "Subscribe to AI Chat"
    App->>FS: GET wallet balance
    FS->>DB: SELECT balance WHERE user_id
    DB-->>FS: Current balance
    FS-->>App: Balance
    alt Sufficient balance
        App->>FS: POST /wallet/subscribe (service=chat)
        FS->>DB: Deduct service cost
        FS->>DB: Insert subscription (valid 30 days)
        DB-->>FS: OK
        FS-->>App: Subscription active until [date]
    else Insufficient balance
        FS-->>App: Error: contact admin to top up
        App-->>U: Show "Balance too low" message
    end
```

The wallet is **administered by the doctor/manager** — no in-app payment gateway in this version.

---

## Security & Privacy

| Concern | Mitigation |
|---|---|
| Unauthorized access | JWT verified on every protected endpoint |
| Password security | bcrypt hashing — no plaintext storage |
| Cross-user data leaks | Supabase RLS scoped to `auth.uid()` |
| AI hallucinations | Safety layer + medical disclaimers + citations |
| Account abuse | Doctor-administered account creation only |
| Sensitive image storage | Supabase Storage with signed URLs |
| Token persistence | flutter_secure_storage on device |
| Wallet fraud | Server-side balance enforcement, all writes audited |

---

## Scalability Notes

- **Stateless Flask** — horizontal scaling via load balancer
- **Supabase Pro** — handles connection pooling and read replicas
- **Gemini** — pay-per-call; cost monitored via wallet system
- **LoRA model** — small enough to serve from a single GPU/CPU node

---

## Test Coverage

Both **white-box** (unit tests via Postman) and **black-box** (use-case driven) tests were documented across 50+ test cases covering:

- Login flows (valid, invalid, locked accounts)
- Account creation by admin
- Wallet operations (top-up, deduction, refund)
- Medical test upload + AI analysis
- Chatbot subscription flow
- Sleep tracking input validation
- Child profile data entry
- Permission middleware enforcement

Full test documentation is part of the project submission to ASPU.
