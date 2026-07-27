# ETF Risk Framework

This project develops a transparent and explainable framework for comparing the different aspects of risk in exchange-traded funds (ETFs).

The model combines historical market risk, holdings concentration, sector exposure, country exposure and currency risk into an overall risk score from 0 to 100.

## Project Aim

The aim of this project is to develop a clear and understandable ETF risk metric for retail investors, enabling them to compare ETFs consistently and identify the key factors driving each fund’s overall risk score.

The framework covers 20 ETFs across:

- Global and regional equities
- Sector-specific equities
- Government bonds
- Corporate bonds
- Gold
- Property

## Risk Dimensions

The overall risk score combines three main components:

### Market Risk — 60%

- Annualised volatility (price movements over a year)
- Maximum drawdown (largest fall from a previous peak to its lowest point)
- 95% Conditional Value at Risk (average loss during the worst 5% of periods)
- Beta relative to VWRP.L (how the ETF moves compared with the global market benchmark)

### Concentration Risk — 30%

- Number of holdings
- Sector concentration
- Country concentration
- Herfindahl–Hirschman Index
- Effective number of exposures

### Currency Risk — 10%

Currency exposure is classified as:

- Low
- Medium
- High

## Overall Scoring Method

Each raw metric is converted to a comparable score from 0 to 100 using min-max normalisation.

The overall score is calculated as:

Overall Risk Score =
60% Market Risk +
30% Concentration Risk +
10% Currency Risk

Higher scores indicate greater comparative risk within the selected ETF universe.

A score of zero does not mean that an ETF has no risk. It means that it has the lowest relative value within this sample.

## Model Validation

The market-risk model was tested using an out-of-sample time split:

- Training period: July 2021 to July 2024
- Testing period: July 2024 to July 2026

The training-period market-risk score was compared with future realised outcomes.

| Future outcome | Pearson correlation | Spearman correlation |
|---|---:|---:|
| Volatility | 0.758 | 0.689 |
| Maximum drawdown | 0.734 | 0.687 |
| CVaR | 0.807 | 0.696 |

All relationships were statistically significant at the 5% level.

The results indicate that ETFs receiving higher training-period risk scores generally experienced greater future downside risk.

## Sensitivity Analysis

Alternative weighting scenarios were tested to determine whether the rankings depended heavily on the selected weights.

The scenarios included:

- Base model
- Volatility-focused
- Downside-focused
- Equal weighting

Most ETFs moved by no more than one to three ranking positions. VGOV.L was the most sensitive ETF, moving by up to five positions.

This suggests that the rankings are broadly stable under reasonable alternative assumptions.

## Repository Structure

data/
    raw/                 Original downloaded data
    processed/           Cleaned data and model outputs

notebooks/
    01_data_collection.ipynb
    02_data_cleaning.ipynb
    03_risk_metrics.ipynb
    04_holdings_metrics.ipynb
    05_exposure_metrics.ipynb
    06_risk_scoring.ipynb
    07_model_validation.ipynb
    08_visual_outputs.ipynb

dashboard/
    app.py                Streamlit dashboard

outputs/
    figures/              Final charts

docs/
    methodology.md
    data_dictionary.md
    limitations.md

    ## Dashboard

The final artefact is a Streamlit dashboard that allows you to:

- View the full ETF risk ranking
- Select and examine individual ETFs
- Compare market, concentration and currency sub-scores
- Identify each ETF's main risk driver
- View the overall risk band and ranking

Run the dashboard locally using:

```bash
python -m streamlit run dashboard/app.py
```

## Main Outputs

The project produces:

- An overall ETF risk score from 0 to 100
- Risk bands from Very Low to Very High
- Market, concentration and currency sub-scores
- A main risk-driver classification
- Sector and country concentration measures
- Out-of-sample validation results
- Sensitivity-analysis results
- A Streamlit comparison dashboard

## Limitations

- The framework compares risk within the selected 20-ETF universe.
- Holdings and exposure data change over time.
- Some bond and specialist ETF exposure data use clearly identified proxies.
- Min-max scores depend on the ETFs included in the sample.
- Historical risk does not guarantee future outcomes.
- The framework is a comparative risk indicator rather than a precise loss forecast.

## Disclaimer

This project is for academic and educational purposes only. It does not constitute financial advice.