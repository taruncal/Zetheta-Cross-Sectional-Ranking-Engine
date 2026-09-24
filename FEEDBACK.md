# Internship Project Feedback & Performance Evaluation
Project 1C: Cross-Sectional Propensity & Stock-Ranking Engine  
Zetheta Algorithms Private Limited (CIN: U62012MH2023PTC410415)  
Author / Intern: Tarun Kumar Das (`@ZethetaIntern`)  

---

## 1. Project Evaluation Summary

Project 1C successfully demonstrated institutional-grade quantitative research, bridging advanced machine learning techniques (LightGBM LambdaRank, Optuna HPO, and conformal prediction) with the practical regulatory and macro constraints of the Indian mutual fund industry.

### Key Performance Indicators Achieved:


Out-of-Sample Rank IC: 0.0111 (Robust predictive signal across time-aware validation folds)
Gross Decile Spread: 1.25% top-bottom monthly spread
Net-of-Cost Spread: 1.00% (incorporating a strict 25 bps Indian market round-trip transaction drag)
Governance Standard: Tamper-evident, hash-chained audit logging ensuring full reproducibility and data lineage compliance.

## 2. Technical & Research Takeaways

Shift from Magnitude to Rank: Moving away from intractable absolute price point forecasts to relative cross-sectional ranking significantly improved signal stability in emerging markets.
Rigorous Point-in-Time Safeguards: Enforcing survivorship bias removal and availability timestamps (`avail_date`) eliminated backtest leakage and ensured realistic execution constraints.
Production-Ready Codebase: Structuring the project into modular components (`src/model.py`, `src/audit.py`, `src/pipeline.py`) alongside automated unit tests (`tests/test_pipeline.py`) meets professional software engineering standards for quantitative desks.

## 3. Conclusion & Next Steps
The delivery of Deliverable 1 (Master Technical Report), Deliverable 6 (Investment Committee Presentation Deck), and the fully structured GitHub repository (`taruncal`) fulfills all requirements for the quantitative research desk handover.

---
*Strictly Private and Confidential | Zetheta Algorithms Private Limited*
