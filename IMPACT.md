# Impact & Theory of Change

This document articulates the social problem BloomBelly addresses, the change pathway it creates, and the metrics by which we measure impact. It is intended for grant reviewers, social-impact investors, and researchers evaluating the project's potential beyond its technical merits.

---

## The Problem We Address

Maternal and child health outcomes in Arabic-speaking and low-resource regions remain among the most unequal in the world. The WHO has identified the period from conception through the first two years of life — the "first 1,000 days" — as the single highest-leverage window for improving lifetime health, cognitive development, and economic outcomes.

Despite the abundance of digital health products globally, the population we serve faces three compounding barriers:

1. **Language and cultural mismatch.** Most well-funded maternal-health apps are designed in English, for high-income contexts. Arabic translations, when they exist, are mechanical — they do not adapt to local clinical conventions, family structures, or the right-to-left reading experience.

2. **Information overload and contradiction.** Pregnant women routinely consult 5–10 sources for any given question, receive contradictory answers, and report measurable anxiety as a result.

3. **Father exclusion.** Cultural and digital design biases together produce a dynamic in which fathers want to be involved but lack a clear role. This is documented in peer-reviewed literature (e.g., *Frontiers in Public Health*, 2022).

A fourth, structural barrier exists for our target users: many lack reliable broadband and continuous access to specialists, making in-clinic resolution of every minor question impractical.

---

## Our Theory of Change

We hypothesize that a well-designed Arabic-first digital companion, anchored in evidence and integrated into the clinic-patient relationship via a doctor-administered access model, can:

```
Improved information access
            ↓
Reduced uncertainty and anxiety
            ↓
Better adherence to clinical recommendations
            ↓
Earlier detection of warning signs
            ↓
Improved maternal and child health outcomes
```

Each arrow in this chain is supported by peer-reviewed literature, summarized below.

### Evidence for Each Link

| Causal Link | Supporting Evidence |
|---|---|
| Information access → reduced anxiety | Multiple studies on self-monitoring during pregnancy (PLOS ONE) |
| Reduced anxiety → adherence | Studies on digital health interventions for chronic conditions |
| Adherence → outcomes (general) | WHO digital health strategy 2020-2025 |
| Fetal movement awareness → outcomes | Saastad et al., PLOS ONE 2011 (kick counting RCT) |
| Partner support → maternal mental health | Versele et al., Frontiers in Public Health 2022 |
| Nutrition guidance → outcomes | King 2016 review on maternal nutrition |

---

## Target Beneficiaries

### Primary
- **First-time mothers** in Arabic-speaking countries (estimated 7M+ pregnancies annually in MENA)
- **Mothers with multiple young children** — particularly those balancing pregnancy with active childcare
- **Mothers in semi-urban and rural areas** with limited specialist access

### Secondary
- **Fathers** seeking structured ways to engage with pregnancy
- **Healthcare providers** (clinics, OB/GYNs, pediatricians) using the wallet/admin features for patient support

### Tertiary
- **Researchers** in maternal health, Arabic NLP, and digital health interventions
- **Health systems** seeking scalable patient-engagement tools

---

## SDG Alignment

BloomBelly directly contributes to:

| UN Sustainable Development Goal | Specific Targets |
|---|---|
| **SDG 3 — Good Health and Well-Being** | 3.1 (maternal mortality), 3.2 (under-5 mortality), 3.7 (reproductive health), 3.8 (universal health coverage) |
| **SDG 5 — Gender Equality** | 5.6 (reproductive rights), 5.b (technology for women's empowerment) |
| **SDG 10 — Reduced Inequalities** | 10.2 (inclusion regardless of language, geography) |
| **SDG 4 — Quality Education** | 4.7 (health literacy) |

---

## Outcome Metrics

We have designed the platform to measure both engagement and clinical outcomes. Specific KPIs include:

### Engagement (proxy for accessibility)
- Daily active users per cohort
- Session length and frequency
- Feature adoption rates per user type
- Drop-off points in onboarding

### Knowledge & behavior change
- Pre/post quizzes on pregnancy knowledge (validated instruments)
- Adherence to recommended kick-counting frequency
- Vaccination schedule completion rates (for mothers with children)
- Nutrition log completeness

### Clinical (long-term, with research partner)
- Early detection rate of warning signs (reduced fetal movement, preeclampsia symptoms)
- Time-to-clinic for red-flag symptoms
- Patient-reported anxiety scores (validated scales)
- Father engagement scores (self-report and partner-report)

### System-level (with health partners)
- Reduction in non-urgent clinic visits for information-seeking questions
- Increased proportion of routine prenatal visits attended on schedule
- Earlier identification of high-risk pregnancies

---

## Risks & Mitigations

| Risk | Mitigation |
|---|---|
| AI misinformation in clinical advice | 4-stage safety pipeline; medical disclaimers; emergency triage; doctor-administered model |
| Data privacy breach | RLS on every table; bcrypt; JWT; PII stripping before AI calls; planned compliance work |
| Digital divide reinforcement | Doctor-distribution model brings the tool to patients who would not self-discover it; offline-first roadmap |
| Cultural/dialect mismatch | Native Arabic content; partnerships with local clinicians for content review |
| Sustainability beyond grant funding | Wallet model creates a clinic-revenue pathway; multiple non-dilutive funding sources targeted |

---

## Sustainability & Scale

BloomBelly is designed for sustainable operation beyond initial grant funding through:

1. **Clinic distribution model** — clinics pay for premium accounts on behalf of their patients
2. **Tiered freemium** — core tracking is free; AI-intensive features (chatbot, image analysis) are wallet-funded
3. **Research partnerships** — anonymized data export (opt-in) for academic collaborations
4. **Multi-country expansion** — the Arabic-first foundation works across the Arab League's 22 member states with minimal localization

---

## Target Funding & Partnership Programs

The project is positioned for the following funding and acceleration tracks:

### Digital Health Grants
- Grand Challenges Canada — *Saving Lives at Birth*
- WHO Digital Health Innovations
- UNICEF Innovation Fund
- Bill & Melinda Gates Foundation — Grand Challenges
- USAID Development Innovation Ventures (DIV)

### MENA-Specific
- Misk Foundation
- Mohammed bin Rashid Foundation (MBRF)
- Sheikha Fatima Initiative (UAE)
- Abdul Latif Jameel Poverty Action Lab (J-PAL MENA)
- Hub71 (Abu Dhabi)

### Accelerators
- Plug and Play Health (Riyadh)
- Flat6Labs
- MIT Solve
- Echoing Green Fellowship

### AI for Good
- Google.org AI for Social Good
- Microsoft AI for Health
- ITU/UN AI for Good Global Summit

---

## Letters of Support

We are actively cultivating letters of support from:

- Our academic supervisors (already committed)
- Domain-expert interviewees (OB/GYNs, pediatricians)
- Pilot users (testimonials being gathered)
- University leadership

Available on request.

---

*Maternal and child health is the single highest-leverage investment any society can make. BloomBelly is our contribution to that investment, built in the region we know best, for the population that has been underserved by global digital health to date.*
