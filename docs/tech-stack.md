# BloomBelly — Tech Stack

The full technical breakdown of the BloomBelly graduation project.

## Mobile Client (Flutter)

| Concern | Choice | Why |
|---|---|---|
| Framework | **Flutter** | Single codebase iOS/Android, strong Arabic typography support, mature ecosystem |
| Language | **Dart** | Null-safety, async/await, records |
| Architecture | **MVVM** | Clean separation of View / ViewModel / Model |
| State Management | **Provider** | Lightweight, reactive, well-supported |
| Routing | **go_router** | Declarative, web-aware, deep-link friendly |
| HTTP | **http** + custom REST clients | Talks to our Flask backend |
| Image handling | **cached_network_image**, **image_picker** | Caching + camera/gallery uploads |
| Charts | **fl_chart** | Growth curves, kick statistics |
| Realtime | **supabase_flutter** | Live wallet balance, multi-device sync |
| Auth storage | **flutter_secure_storage** | Token persistence |

## Backend (Python Flask)

| Concern | Choice | Why |
|---|---|---|
| Framework | **Flask** | Lightweight, ideal for AI orchestration |
| Language | **Python 3.x** | Native ecosystem for ML/AI libraries |
| Auth | **JWT (JSON Web Tokens)** | Stateless, easy to scale |
| Password hashing | **bcrypt** | Industry standard |
| API style | **RESTful** | Predictable, well-understood |

## AI / ML Stack

| Component | Technology | Purpose |
|---|---|---|
| **Medical image analysis** | Google Gemini API | Analyzes lab results, ultrasounds, prenatal images |
| **Conversational AI** | Fine-tuned transformer (Hugging Face) | Pregnancy/childcare Q&A chatbot |
| **Tuning technique** | LoRA (Low-Rank Adaptation) | Efficient specialization of base model |
| **ML framework** | PyTorch | Model loading and inference |
| **Nutrition classifier** | Random Forest (scikit-learn) | Evaluates meal suitability per pregnancy stage |
| **Data processing** | Pandas + NumPy | Feature engineering and validation |

### Why this AI mix?

We deliberately did **not** use one model for everything:

- **Gemini** is multimodal and handles images well — best for medical scans.
- **LoRA-tuned transformer** is cheap to train, lightweight to serve, and gives the chatbot domain depth.
- **Random Forest** is interpretable, deterministic, and easy to retrain — perfect for the nutrition feature where rules matter.

## Database & Cloud

| Layer | Technology | Notes |
|---|---|---|
| Database | **Supabase Postgres** | Free tier sufficient for pilot; supports RLS |
| Auth | **Supabase Auth** | Email-based; integrated with our doctor-administered flow |
| Storage | **Supabase Storage** | Medical images, profile photos, signed URLs |
| Realtime | **Supabase Realtime** | Wallet updates, sync across devices |

Database schema includes 15+ tables: `users`, `manager`, `pregnancies`, `children`, `fetal_moves`, `pregnancy_weight`, `nutrition`, `medical_tests`, `vaccine`, `sleep_test`, `growth`, `wallet_tx`, `transaction`, `care_guides`, `weekly_templates`, `suggestions`, plus a `pregnancy_father_videos` content table.

## DevOps & Quality

| Tool | Purpose |
|---|---|
| **GitHub** | Source control, branching, code review |
| **Jira** | Sprint planning, backlog, task tracking |
| **Postman** | API testing & documentation |
| **Figma** | UI/UX design (full design system + prototype) |
| **Telegram** | Team coordination & supervisor updates |
| **VS Code** | Primary IDE |

## Why NOT these alternatives?

| Alternative | Why we passed |
|---|---|
| React Native | Less mature Arabic typography; smaller ecosystem for our use case |
| Firebase | Strong, but Supabase free tier is more generous and Postgres is more familiar |
| Firebase ML Kit | Doesn't cover medical-image analysis at the depth Gemini does |
| OpenAI GPT-4 | Stronger English, but cost and Arabic support weaker for our budget |
| Hive (local DB) | Not needed in V1; all state lives server-side |
| Riverpod / BLoC | More boilerplate than Provider for our complexity level |
| Full transformer retraining | Far too expensive for a student project; LoRA gives us 80% of the benefit at 5% of the cost |

## Fonts

Arabic fonts bundled in-app:
- Amiri (body)
- Cairo (UI)
- Mirza (callouts)
- Harmattan (alternate body)
- Gulzar (decorative)

Plus Playwrite US Traditional for English handwritten accents.

## References

The project is grounded in 17+ peer-reviewed sources spanning maternal-child health, digital health interventions, nutrition during pregnancy, fetal movement counting, pediatric sleep, and partner support — all detailed in the thesis bibliography.
