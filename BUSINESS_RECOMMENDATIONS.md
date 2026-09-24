# Strategic Business Recommendations & Execution Roadmap
Project 1C: Cross-Sectional Propensity & Stock-Ranking Engine 
Zetheta Algorithms Private Limited (CIN: U62012MH2023PTC410415) 

---

## 1. Executive Implementation Strategy
Based on the out-of-sample empirical findings (achieving a **Mean Rank IC of 0.0111** and a **1.00% Net-of-Cost Decile Spread**), the Investment Committee is advised to transition Project 1C from staging into live alpha generation under the following phased framework:

Phase 1: Satellite Alpha Overlay: Deploy the model initially as a quantitative screening overlay for existing mid-cap and large-cap active mutual fund schemes, restricting turnover to monthly rebalance schedules.
Phase 2: Dynamic Constraint Integration: Couple the LightGBM LambdaRank conviction scores directly with portfolio optimizer risk constraints (tracking error caps <= 4% and maximum sector active weights <= +/-2%).

## 2. Risk Management & Friction Mitigation
Transaction Cost Budgeting: The backtest incorporates a conservative **25 bps round-trip transaction drag**. Execution desks must utilize VWAP (Volume Weighted Average Price) execution algorithms during monthly rebalance windows to minimize market impact in less liquid Nifty 500 constituents.
Conformal Shortlist Safeguards: Leverage the split-conformal prediction threshold (q-hat = 0.5045) as a dynamic risk gate to filter out low-conviction names during high-volatility macro regimes.

## 3. Future Quantitative R&D Roadmap
1. Alternative Data Integration: Incorporate institutional sentiment shifts and supply-chain alternative data feeds into the six core feature families.
2. Ensemble Expansion: Extend the single-engine LightGBM architecture with transformer-based cross-sectional attention networks for non-linear interaction discovery.

---


*Strictly Private and Confidential | Zetheta Algorithms Private Limited*
