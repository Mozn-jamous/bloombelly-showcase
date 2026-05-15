# BloomBelly — Case Study

## Context

This project was developed as our **graduation thesis** at the **Informatics Engineering College, Al-Sham Private University (ASPU)** in Damascus, Syria, for the academic year 1447 AH / 2026 CE.

It was authored jointly by **Mozn Jamous** and **Shahd Bureghsh**, under the supervision of **Dr. Afaf Al-Shalabi** and **Eng. Rahaf Abdul Qader**.

The work addresses a gap we observed firsthand in our community: Arabic-speaking pregnant women lack a single digital companion that respects their language, organizes their care, and supports their families through pregnancy and early childhood.

## The Problem

Through stakeholder interviews with OB/GYNs, pediatricians, nutritionists, and dozens of mothers, we identified five recurring pain points:

1. **Information overload and contradiction.** A typical question — "is this food safe in week 24?" — produces a dozen conflicting answers from different forums and translated articles.

2. **Disorganized clinical follow-up.** Test results and appointments live in WhatsApp screenshots, paper notebooks, and memory. Important findings get lost between visits.

3. **The double burden of mothers with a young child.** They juggle pregnancy with active childcare (vaccinations, sleep tracking, growth monitoring) — and no single tool helps them do both.

4. **Father exclusion.** Many fathers want to engage but don't know how. Existing apps cater to the mother alone, leaving the partner without a clear role.

5. **Generic, decontextualized advice.** Recommendations don't adapt to the mother's specific stage, conditions (gestational diabetes, anemia), or cultural context.

## The Approach

### Doctor-administered access

We chose a **Manager (doctor) role** to create user accounts rather than self-registration. This adds clinical oversight, ensures verified users, and aligns with how care is delivered in our region. It also enables a **wallet-based paid-services model** managed offline by the clinic — no in-app payment gateway needed in V1.

### MVVM on Flutter, Flask on the server

The mobile client uses **MVVM with Provider** for clean separation between view, view-model, and model. The backend is **Python Flask** — a deliberate choice because it lets us host three different AI systems (Gemini, a LoRA fine-tuned transformer, and a Random Forest classifier) behind one unified API.

### Three AI components, each for its job

We didn't try to use one model for everything. Instead:

- **Google Gemini** for medical image analysis (lab results, ultrasounds) because its multimodal vision is strong and the API economics work for a graduation-scale project.
- **LoRA fine-tuning** of a transformer model for the medical chatbot — small enough to serve, specialized enough to answer pregnancy questions credibly with citations.
- **Random Forest classifier** for nutrition evaluation — interpretable, fast, and easy to retrain when guidelines update.

### Evidence-based content

Every clinical claim in the app links to a research foundation:

| Feature | Reference |
|---|---|
| Kick counter | ACOG "Count the Kicks" — 10 movements in 2 hours |
| Reduced movement awareness | Studies in *PLOS Global Public Health* & *BJOG* |
| Sleep recommendations | American Academy of Sleep Medicine |
| Vaccination schedule | Syrian Ministry of Health |
| Maternal nutrition | WHO guidelines on pregnancy nutrition |
| Father involvement design | *Frontiers in Public Health* research |

The bibliography in our thesis lists 17+ peer-reviewed sources.

### Arabic-first design

The UI, content, and chatbot are designed for Arabic from day one. The chatbot accepts Arabic input, even though responses are rendered in English in this version (a future iteration will switch to native Arabic responses).

## Trade-offs

| Decision | Trade-off |
|---|---|
| Flask backend instead of Supabase Edge Functions | More infrastructure to host, but full control over AI orchestration |
| Doctor-administered accounts | Slower onboarding, but adds clinical credibility & prevents abuse |
| Wallet system instead of payment gateway | Limits to clinic distribution in V1, but bypasses regional payment complexity |
| LoRA fine-tuning over full retraining | Less model "depth", but vastly cheaper to train and serve |
| English chatbot output | Easier model training, but suboptimal UX — to be fixed in V2 |
| Provider over Riverpod / BLoC | Lower ceiling for complex state, but enough for our use cases |

## Outcome

- **Functional MVP** with all 4 user roles, AI image analysis, fine-tuned chatbot, nutrition classifier, kick counter, wallet system, and child-care features
- **50+ test cases** documented (both white-box and black-box)
- **Full system documentation** including ERD, class diagrams, sequence diagrams, use cases, and architectural decision records — submitted as part of the graduation thesis
- **Stakeholder validation** through interviews with mothers, fathers, OB/GYNs, pediatricians, and nutritionists
- **Pilot use** by friends and family during development

## What We Learned

- **AI orchestration is its own engineering problem.** Combining Gemini + LoRA + Random Forest meant building safety layers, fallbacks, and cost controls that aren't taught in a single ML course.
- **Doctor-administered accounts changed the entire UX.** We initially designed self-registration, then realized the clinic distribution model gave us trust, oversight, and a clean monetization path simultaneously.
- **Stakeholder interviews exposed assumptions we didn't know we had.** Fathers don't want to be passive observers — they want a clear role. Mothers with a child don't want a second app for the older one; they want everything in one place.
- **Evidence-based design is a feature.** Linking every recommendation to a peer-reviewed source built credibility with our supervisors and gave us a defensible position when reviewers asked "why do you say this?"
- **Co-authorship demands tight coordination.** Working with [@shahd-bureghsh] taught us the value of daily syncs, clear role splits, and shared JIRA boards.

## What's Next

- **Public beta release** on App Store and Play Store
- **Native Arabic chatbot output** (currently English-only)
- **Contraction timer** and **breastfeeding tracker** for V2
- **Direct integration** with clinic appointment systems
- **Anonymized data export** for research partners (opt-in)
- **Submission to grants** targeting maternal/child health in MENA: Grand Challenges Canada, UNICEF Innovation Fund, Misk Foundation, Plug and Play Health
- **Academic publication** of the LoRA fine-tuning approach for Arabic medical Q&A

---

*Submitted to Al-Sham Private University, College of Informatics Engineering, 2026.*
