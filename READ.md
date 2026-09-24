Zetheta Algorithms Private Limited (CIN: U62012MH2023PTC410415)

Project 1C: Cross-Sectional Propensity & Stock-Ranking Engine

Role: Data Quantitative Analyst — Equity Research & Quant Strategies Desk


---




1. Executive Summary & Core Thesis

Modern quantitative research in Indian equity markets faces a structural transformation. With the Indian mutual fund industry crossing ₹70 lakh crore in AUM and monthly Systematic Investment Plan (SIP) inflows exceeding ₹26,000 crore, domestic institutional investors (DIIs) have become the dominant marginal price-setting force[cite: 3]. In this environment of alpha compression and Total Expense Ratio (TER) compression, traditional price-magnitude forecasting ("HDFC Bank will rise 8% this year") fails due to extreme idiosyncratic noise and non-stationary market regimes [cite: 3].

This project implements the Direction-and-Ranking-Over-Magnitude thesis[cite: 3]. Rather than attempting the unanswerable task of predicting absolute price levels, the engine solves a tractable discrimination problem: ranking which stocks are most likely to out-perform their cross-sectional peers over a forward holding horizon [cite: 3]. 

The engine delivers a single, unified score per name on each date that serves a dual purpose[cite: 3]:

A. The Conviction Ordering: A cross-sectional rank utilized by portfolio managers to construct top-N shortlists [cite: 3].

B. The Calibrated Propensity: A post-processed probability P(out-perform) that reflects true empirical frequencies and guides conviction-based position sizing [cite: 3].





---




2. Technical Architecture & Methodology

A. Point-in-Time Discipline & Universe Construction

Survivorship Safety: To eliminate survivorship bias, the investment universe is reconstructed as-of each historical date, preserving delisted, merged, or bankrupt names to ensure realistic backtest evaluations [cite: 3].

Look-Ahead Controls: Fundamental inputs are availability-dated and joined via point-in-time as-of logic. Forward relative-return labels are computed using prices strictly after the feature generation window [cite: 3].



B. Feature Engineering & Neutralisation

Features are drawn from six core institutional families [cite: 3]:

Value: Earnings yield, book-to-price, FCF yield, EV/EBITDA z-score [cite: 3].

Momentum: 12-1 month return, 3-month return, 52-week high proximity [cite: 3].

Quality: ROE, ROCE, accruals, debt-to-equity, earnings stability [cite: 3].

Growth & Revisions: Sales growth, EPS-estimate revision breadth, surprise [cite: 3].

Low-Risk: Trailing beta, idiosyncratic volatility, drawdown [cite: 3].

Flow & Microstructure: Delivery percentage, FII/DII holding changes, average daily value (ADV) [cite: 3].


Cross-Sectional Standardisation & Neutralisation: Raw features are winsorised (plus or minus 3 standard deviations) and converted to cross-sectional z-scores within each date bucket, then residualised against sector dummies and log-market-cap [cite: 3].




C. Machine-Learning Core: LightGBM LambdaRank

Listwise Optimisation: The engine utilises LightGBM's LambdaRank (LambdaMART) objective with date-grouped query structures [cite: 3]. 


By optimising directly for Normalized Discounted Cumulative Gain (NDCG at K), the model focuses its learning capacity on the head of the ranked list where shortlists are actually constructed [cite: 3].


Skill Quantification: Model quality is certified by an out-of-sample Rank Information Coefficient (IC) evaluation layer, measuring Spearman rank correlation between predicted scores and realised forward relative returns [cite: 3].



D. Probability Calibration & Conformal Selection

Isotonic Regression Calibration: Gradient-boosted raw scores are pushed toward extremes; post-hoc calibration via Isotonic Regression maps scores into trustworthy probabilities where a stated 70% propensity equates to a 70% empirical realisation rate [cite: 3].


Split-Conformal Shortlist Selection: Applying a split-conformal wrapper with a target error rate (alpha = 0.2), establishing a finite-sample-valid non-conformity threshold (q_hat = 0.5273) to admit names into an error-controlled likely out-performer set [cite: 3].



E. Backtesting & Cost Attribution

Decile Spread Analysis: Rebalance dates form decile portfolios to measure the return spread between top (D10) and bottom (D1) buckets [cite: 3].

Transaction Cost Integration: Gross decile spreads are netted against a 25 bps round-trip Indian transaction and impact cost assumption (encompassing brokerage, STT, stamp duty, exchange charges, and market impact) [cite: 3].




---




3. Repository Structure

```text
├── src/
│   ├── project_1c_ranking_engine.py      # Core LightGBM LambdaRank & PIT Feature Pipeline
│   ├── project_1c_calibration.py         # Isotonic Regression Calibration & Split-Conformal Wrapper
│   └── project_1c_backtest.py            # Decile Portfolio Backtester & Net Spread Attribution
├── outputs/                              # Generated evaluation artefacts, metrics, and models
├── requirements.txt                      # Pinned dependencies for reproducible execution
└── README.md                             # Institutional documentation and handover guide












































































