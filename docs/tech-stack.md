# BloomBelly — Tech Stack

A detailed breakdown of every technology choice and its rationale.

## Client (Mobile App)

| Concern | Choice | Why |
|---|---|---|
| Framework | Flutter 3.24+ | Single codebase iOS/Android/Web; mature ecosystem; great Arabic typography support |
| Language | Dart 3.5+ | Null-safety, records, patterns, sealed classes |
| State Management | Riverpod 2.x | Type-safe, testable, code-gen support, no BuildContext dependency |
| Routing | go_router 16 | Declarative, deep-link friendly, web-aware |
| Local Database | drift | Type-safe SQL, reactive streams, code-gen, free + open source |
| Code Generation | freezed + json_serializable + drift_dev + riverpod_generator | Immutable data classes, sealed unions, zero-boilerplate |
| Forms / Validation | flutter_hooks (selectively) | Reduces stateful boilerplate |
| Charts | fl_chart | Native, customizable, performant |
| Caching | cached_network_image | Avatar/photo caching |
| Date / i18n | intl 0.20 | Arabic calendar/format support |
| Secure Storage | flutter_secure_storage | Token persistence |
| Linting | very_good_analysis | Strict, industry-standard ruleset |

## Backend (Supabase)

| Concern | Choice | Why |
|---|---|---|
| Database | Supabase Postgres | RLS, JSONB, full SQL, free tier sufficient for pilot |
| Auth | Supabase Auth + Sign in with Apple | Email + Apple coverage; Apple required for App Store |
| Storage | Supabase Storage | S3-compatible, integrated with RLS |
| Realtime | Supabase Realtime | Streamed updates for cross-device sync |
| Edge Functions | Deno-based (Supabase) | Complex logic outside the client (analytics, AI orchestration) |
| Security | Row Level Security | Every row scoped to `auth.uid()` — enforced at DB layer |
| Migrations | Supabase CLI | Versioned, reproducible schema changes |

## AI Layer

| Concern | Choice | Why |
|---|---|---|
| LLM Provider | Google Gemini (google_generative_ai) | Strong Arabic, generous free tier, cost-effective |
| Safety | Custom 4-stage pipeline | Pre-filter + triage + system prompt + post-filter |
| Prompt Engineering | Hand-tuned + tested vs. seed cases | Maternal/child scope, citations, disclaimers |

## DevOps & Quality

| Concern | Choice | Why |
|---|---|---|
| Version Control | Git + GitHub | Standard; GitHub for CI/CD |
| CI | GitHub Actions | Free for public projects, simple YAML |
| Tests | flutter_test + mocktail + integration_test | Three layers of coverage |
| Code formatting | dart format | Standard tooling |
| Performance | DevTools + Sentry (planned) | Crash + performance monitoring |

## Why NOT these alternatives?

| Alternative | Why we passed |
|---|---|
| React Native | Less mature Arabic typography; web parity weaker for this use case |
| Firebase | Excellent, but pricing scales aggressively; Supabase free tier more generous |
| OpenAI GPT-4 | Stronger English; weaker Arabic in our tests; higher per-token cost |
| Hive (NoSQL) | Fine for simple data, awkward for the relational queries we need |
| Provider | Used originally (via FlutterFlow). Becoming Riverpod in refactor for type safety |
| Bloc | More boilerplate; Riverpod gives us same testability with less code |
| Firebase Auth | Migration story to Supabase is complex; staying with Supabase Auth |

## Fonts

Five Arabic fonts bundled in-app for distinct moods:

| Font | Used for | Why |
|---|---|---|
| Amiri | Body text | Highly legible, classical proportions |
| Cairo | Headings, UI labels | Modern, geometric, clear |
| Mirza | Warm callouts, CTAs | Soft personality |
| Harmattan | Subtle body alternatives | Compact, balanced |
| Gulzar | Decorative moments | Distinctive flourish |

Plus the **Playwrite US Traditional** family for English handwritten accents on certain pages.
