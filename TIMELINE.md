# Project Timeline & Milestones

The development of BloomBelly followed an **Agile methodology** with weekly sprints, supervised reviews, and structured deliverables culminating in the graduation defense.

---

## High-Level Phases

```
2025                           2026
 │                              │
Mar━━ Planning & Research       Sep ─ Final Submission
  ├── Apr ─ Requirements          │
  │    ├── Analysis               │
  │    └── Stakeholder interviews │
  │                               │
  └─ May ━━ Design                │
        │                         │
        ├── Aug ━━ Implementation │
        │     │                   │
        │     └── Testing ━━━━━━━━┤
        │                         │
        └── Sep ━━ Documentation & Defense
```

---

## Detailed Milestones

| # | Phase | Start | End | Duration |
|---|---|---|---|---|
| 1 | Theoretical Study | 2025-03-01 | 2025-03-14 | 14 days |
| 2 | Requirements Elicitation | 2025-03-15 | 2025-03-31 | 17 days |
| 3 | System Analysis | 2025-04-01 | 2025-04-19 | 19 days |
| 4 | Evaluation & Design | 2025-04-20 | 2025-05-03 | 14 days |
| 5 | Implementation (Operational Excellence) | 2025-05-04 | 2025-07-11 | 69 days |
| 6 | Testing | 2025-07-12 | 2025-08-08 | 28 days |
| 7 | Final Documentation | 2025-08-09 | 2025-08-29 | 21 days |
| 8 | Final Review & Defense Prep | 2025-08-30 | 2025-09-02 | 4 days |
| **Final Submission Date** | | | **2025-09-12** | |

(Phase 8 extended through additional iterations into 2026 for thesis defense and refinement.)

---

## Sprint Cadence

We worked in **1- to 2-week sprints** with the following rituals:

- **Sprint planning** — Sunday morning
- **Daily check-ins** — async via Telegram channel with supervisors
- **Mid-sprint sync** — Wednesday voice call
- **Sprint review & demo** — End of sprint, with supervisor present
- **Retrospective** — Same session as review

Task tracking via **Jira**.

---

## Notable Decision Points

| Date | Decision | Outcome |
|---|---|---|
| April 2025 | Adopt MVVM over BLoC | Faster team ramp-up |
| May 2025 | Choose Python Flask backend | Enabled AI orchestration |
| June 2025 | Apply LoRA fine-tuning over RAG | Better domain specialization for budget |
| June 2025 | Doctor-administered account model | Defined the entire distribution strategy |
| July 2025 | Add wallet system | Solved monetization without payment gateways |
| August 2025 | Multi-language tested (Arabic input, English output) | Identified V2 priority: native Arabic output |

---

## Key Deliverables Submitted

By the final submission date, the following artifacts were delivered:

- ✅ Functional mobile MVP across all 4 user roles
- ✅ Python Flask backend with AI orchestration
- ✅ Supabase schema (15+ tables) with RLS policies
- ✅ Three AI components in production (Gemini, LoRA, Random Forest)
- ✅ 50+ documented test cases (black-box + white-box)
- ✅ Full Figma design system and prototype
- ✅ Complete thesis document (~120 pages)
- ✅ ERD, sequence diagrams, class diagrams, use case diagrams
- ✅ Architecture documentation and engineering decision records
- ✅ Stakeholder interview summaries
- ✅ Pilot user feedback report

---

## Post-Graduation Roadmap

The thesis submission is the beginning, not the end. The post-graduation roadmap includes:

### Q4 2025 – Q1 2026
- [ ] Convert source from FlutterFlow scaffolding to clean Flutter
- [ ] Add automated test coverage (target: 60%+ on Domain layer)
- [ ] Set up CI/CD pipeline
- [ ] Public APK release for early testers

### Q2 2026
- [ ] App Store submission
- [ ] Play Store submission
- [ ] First clinic partnership (Damascus)
- [ ] Whitepaper publication

### Q3 2026
- [ ] Grant applications cycle (Grand Challenges, UNICEF, Misk)
- [ ] Pre-seed fundraising
- [ ] 5-clinic pilot in Levant region
- [ ] Native Arabic chatbot output (V2 of LoRA training)

### Q4 2026 – 2027
- [ ] Gulf region expansion
- [ ] Research partnership announcements
- [ ] Seed round
- [ ] Hospital-tier integration

---

## Lessons Learned

A few takeaways from running this timeline:

1. **The implementation phase always expands.** We allocated 69 days; we used every one of them.
2. **Testing benefited from being a dedicated phase.** Treating it as a sprint instead of a side activity caught issues we would have missed.
3. **Documentation early saved time later.** ADRs written during decisions are far easier than reconstructed from memory.
4. **Stakeholder interviews shaped scope.** Without them, we would have over-built features that didn't matter.
