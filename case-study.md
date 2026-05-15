# BloomBelly — Case Study

## Context

In Arabic-speaking countries, mothers face a digital health information gap that is rarely addressed by mainstream maternal-child health apps. Most popular apps (Flo, Ovia, BabyCenter) are designed for English-speaking, well-connected users in the Global North. Translations, when they exist, are mechanical — they don't account for the right-to-left layout, cultural references, or healthcare context of MENA mothers.

Meanwhile, maternal and child mortality in the region remains a serious public health concern. The WHO has highlighted that **timely access to evidence-based information** is one of the most cost-effective interventions to improve outcomes.

## The Challenge

How do you build a digital companion that:

1. Speaks fluent Arabic — not just text, but the *culture* of care?
2. Works reliably in regions with intermittent connectivity?
3. Stays safe when an AI is answering medical questions?
4. Combines pregnancy, postpartum, and child care into one experience?
5. Earns trust as a credible health source, not just another tracking app?

## The Approach

I designed BloomBelly around five core principles:

### 1. Arabic-first design

Five Arabic fonts (Amiri, Cairo, Mirza, Harmattan, Gulzar) bundled in-app, chosen for their distinct moods — Amiri for body text, Cairo for headings, Mirza for warm callouts. The entire UI is built RTL-first; the English version is the translation, not the other way around.

### 2. Evidence-based content

Every tracker is anchored in an external guideline:
- Kick counter → ACOG's "Count the Kicks" methodology (10 in 2 hours)
- Vaccination schedule → WHO Expanded Programme on Immunization
- Growth curves → WHO 2006 Child Growth Standards (LMS z-scores)
- Risk screening (planned) → EPDS for postnatal depression

### 3. Clean, layered architecture

A Strangler Fig refactor is currently underway, migrating from a FlutterFlow-origin codebase to **Clean Architecture + Riverpod + drift + freezed**. Each feature is a self-contained module with Domain, Data, and Presentation layers — independently testable and replaceable.

### 4. Local-first sync

drift (SQLite) is the source of truth on the device. Supabase serves as a syncing backend, not a hard dependency. The app is fully functional offline; writes queue until connectivity returns.

### 5. AI safety as a first-class concern

The Gemini integration is wrapped in a 4-stage safety pipeline: pre-filter for PII and blocked topics, emergency triage for red-flag keywords, system-prompt anchoring during the model call, and post-filter that enforces citations and medical disclaimers.

## Trade-offs

| Decision | Trade-off |
|---|---|
| Local-first DB | More complexity in conflict resolution vs. cloud-only |
| Bundling 5 Arabic fonts | Bigger app size (+8 MB) vs. typographic quality |
| Strangler Fig refactor | Slower than full rewrite vs. zero downtime during migration |
| Riverpod over BLoC | Some boilerplate vs. less codegen friction |
| Gemini over OpenAI | Lower cost & better Arabic vs. ecosystem maturity |

## Outcome (current state)

- Functional MVP with 30+ pages and ~40,000 lines of Dart
- Friends-and-family pilot underway
- Phase 1 of the refactor in execution (Kick Counter as reference feature)
- Whitepaper and Pitch deck in preparation for grant submissions

## What I Learned

- **FlutterFlow accelerates start; it slows down growth.** The same boilerplate that gave the project its first prototype is now the biggest source of friction in the refactor.
- **AI safety in Arabic is under-researched.** English content has multiple medical-safety datasets; Arabic content is sparser. Some safety rules had to be designed from scratch.
- **The pilot teaches more than the prototype.** Even with a handful of users, real feedback exposed assumptions I would have defended for months in isolation.

## What's Next

- Complete Phase 1 of refactor (Kick Counter on Clean Architecture)
- Implement Risk Screening feature (EPDS, PPD, gestational-diabetes red flags)
- Wire WHO Growth Standards into the child growth charts
- Add offline-mode integration tests
- Submit to Grand Challenges Canada (Saving Lives at Birth)
- Public beta launch on Play Store + App Store
