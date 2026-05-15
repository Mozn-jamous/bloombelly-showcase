# Press Kit

This folder contains shareable assets for journalists, grant reviewers, accelerators, investors, and partners interested in BloomBelly.

## Files

| File | Use |
|---|---|
| `BloomBelly-Press-Kit.pdf` | **Single-page PDF** — share with grant reviewers, journalists, accelerators |
| `one-pager.md` | Markdown source for the press kit content |
| `generate_press_kit_pdf.py` | Script that builds the PDF (uses `reportlab`) |

## Quick Use

1. **Reviewing the project for a grant?** Open `BloomBelly-Press-Kit.pdf` first — it contains everything you need to evaluate the opportunity in one page.
2. **Writing about the project?** Use `one-pager.md` as a quote source and the [main README](../README.md) for technical depth.
3. **Investor due diligence?** Pair this kit with [BUSINESS-MODEL.md](../BUSINESS-MODEL.md), [IMPACT.md](../IMPACT.md), and [ENGINEERING-DECISIONS.md](../docs/ENGINEERING-DECISIONS.md).

## Press Contact

**Mozn Jamous**
asaierafi@clinlab.ai
linkedin.com/in/mozn-jamous

## Regenerating the PDF

```bash
pip install reportlab
python generate_press_kit_pdf.py
```

## Key Facts (for fast reference)

- **Project name:** BloomBelly
- **Type:** Mobile health platform (Flutter)
- **Audience:** Arabic-speaking mothers, fathers, and clinics in MENA
- **Institution:** Al-Sham Private University (ASPU), Damascus
- **Year:** 2026 graduation thesis
- **Authors:** Mozn Jamous (Backend, AI, Architecture) & Shahd Bureghsh (Frontend, UX, Product)
- **Supervisors:** Dr. Afaf Al-Shalabi (Principal) · Eng. Rahaf Abdul Qader (Technical)
- **Tech stack:** Flutter · Python Flask · Google Gemini · LoRA · Random Forest · Supabase
- **Status:** Functional MVP submitted as thesis; preparing for public beta + grant applications
