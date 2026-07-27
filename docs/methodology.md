# Methodology

## 1. Project Overview

This project develops a transparent and explainable framework for comparing the risk of 20 exchange-traded funds (ETFs).

The selected ETFs includes:

- Broad and regional equity ETFs
- Sector-focused equity ETFs
- Government bond ETFs
- Corporate bond ETFs
- Gold
- Property

Each ETF receives an overall comparative risk score from 0 to 100.

Higher scores indicate greater risk relative to the other ETFs in the selected universe.

## 2. Data Sources

The framework uses two main categories of data:

### Historical market data

Five years of daily closing prices were collected using the `yfinance` Python library.

With this historical price data the following were able to be calculated:

- Daily returns: Daily returns show how much an ETF’s price increases or decreases each day. They are important because they are used to calculate other risk measures and help identify how frequently the ETF experiences gains or losses.
  
- Annualised volatility: Annualised volatility shows how much an ETF’s returns typically change over a year. A higher volatility means the ETF’s price moves more sharply, which generally indicates greater risk.

- Maximum drawdown: Maximum drawdown measures the largest fall in an ETF’s value from its highest point to its lowest point. It is important because it shows how much an investor could have lost during the ETF’s worst period.

- Value at Risk (VaR): Value at Risk estimates the potential loss an ETF could experience over a certain period at a chosen confidence level. It helps investors understand how much they could lose under unusually poor market conditions.

- Conditional Value at Risk (CVaR): Conditional Value at Risk measures the average loss when returns fall within the worst-performing periods. It is important because it shows how severe losses could be when the VaR estimate is exceeded.

- Beta: Beta measures how sensitive an ETF is to movements in a market benchmark. A beta above one means the ETF normally moves more than the market, while a beta below one suggests that it is less sensitive.

### Holdings and exposure data

Holdings and exposure information was collected from official ETF providers and index providers where available.

The data includes:

- Number of holdings
- Sector allocations
- Country allocations
- Main currency exposure
- Currency-risk classification

Each exposure record includes:

- Data-as-of date
- Source URL
- Source-quality classification
- Notes describing any assumptions or proxies

Data-quality warning: Some exposure data was initially gathered with the assistance of AI tools. Although the information was checked against available official sources, some values may rely on estimates, proxies or incomplete disclosures. 

## 3. Data Preparation

ETF price series were aligned into a common date index.

Small missing-price gaps were forward-filled. These gaps were mainly caused by differences in exchange holidays and trading calendars.

Daily returns were calculated as:

```text
Daily Return = (Current Price / Previous Price) - 1
```

The corrected and cleaned datasets were saved in the `data/processed` directory.

## 4. Market-Risk Measures

### 4.1 Annualised Volatility

Daily return standard deviation was annualised using 252 trading days:

```text
Annualised Volatility =
Standard Deviation of Daily Returns × √252
```

Higher volatility indicates greater variation in historical returns.

### 4.2 Maximum Drawdown

Maximum drawdown measures the largest percentage fall from a previous peak.

```text
Drawdown =
(Current Cumulative Value / Previous Peak Value) - 1
```

The most negative drawdown observed during the period is the maximum drawdown.

For scoring purposes, the absolute size of the loss was used.

### 4.3 Value at Risk

Historical 95% Value at Risk represents the loss threshold exceeded during approximately the worst 5% of daily observations.

```text
95% VaR = 5th percentile of daily returns
```

### 4.4 Conditional Value at Risk

Conditional Value at Risk measures the average loss during observations that fall below the 95% VaR threshold.

```text
95% CVaR =
Average daily return during the worst 5% of observations
```

For scoring purposes, CVaR was converted into a positive loss magnitude.

### 4.5 Beta

Beta measures sensitivity to movements in the selected market benchmark.

`VWRP.L`, the Vanguard FTSE All-World UCITS ETF, was used as the benchmark.

```text
Beta =
Covariance between ETF and benchmark returns
÷
Variance of benchmark returns
```

Negative beta values were treated as zero when constructing the market-risk score.

This prevents negative market relationships from being interpreted as negative risk.

## 5. Concentration-Risk Measures

### 5.1 Number of Holdings

The number of holdings provides a simple diversification indicator.

A logarithmic transformation was applied because the difference between 20 and 100 holdings is generally more meaningful than the difference between 2,000 and 2,080 holdings.

```text
Log Holdings = log(1 + Number of Holdings)
```

ETFs with fewer holdings receive higher holdings-count risk scores.

This is treated as a diversification proxy rather than a complete measure of concentration.

### 5.2 Sector Concentration

Sector concentration was calculated for the 12 applicable equity ETFs.

Bond, gold and property ETFs were excluded from the standard equity-sector calculation.

### 5.3 Country Concentration

Country or geographic concentration was calculated for 19 ETFs.

The physical gold ETC was excluded because it does not have a conventional country allocation.

Some bond and specialist ETF country figures use explicitly identified proxies where complete official look-through data was unavailable.

### 5.4 Herfindahl–Hirschman Index

Sector and country concentration were measured using the Herfindahl–Hirschman Index.

```text
HHI = Sum of Squared Exposure Weights
```

Weights were converted from percentages into decimals before being squared.

An ETF with a single 100% exposure has:

```text
HHI = 1.00
```

A more evenly distributed ETF has a lower HHI.

### 5.5 Effective Number of Categories

The effective number of sectors or countries was calculated as:

```text
Effective Categories = 1 / HHI
```

This estimates how many equally weighted categories would produce the same level of concentration.

## 6. Currency Risk

Currency exposure was converted into a transparent categorical score:

| Currency-risk level | Score |
|---|---:|
| Low | 25 |
| Medium | 50 |
| High | 75 |

This measure reflects the relative currency-risk category assigned to each ETF.

It is a simplified indicator and does not model daily exchange-rate volatility directly.

## 7. Normalisation

Raw risk measures use different units and scales.

Each measure was converted to a 0–100 score using min-max normalisation:

```text
Normalised Score =
100 × (Value - Minimum)
÷
(Maximum - Minimum)
```

A score of zero indicates the lowest observed value within the selected ETF sample.

A score of 100 indicates the highest observed value within the selected ETF sample.

These scores are relative and will change if the ETF universe changes.

## 8. Market-Risk Sub-Score

The market-risk score combines four measures:

| Measure | Weight |
|---|---:|
| Annualised volatility | 30% |
| Maximum drawdown | 30% |
| CVaR | 25% |
| Beta | 15% |

```text
Market Risk Score =
30% Volatility Score
+ 30% Drawdown Score
+ 25% CVaR Score
+ 15% Beta Score
```

## 9. Concentration-Risk Sub-Score

The concentration-risk score combines:

| Measure | Weight |
|---|---:|
| Holdings-count risk | 40% |
| Sector concentration | 30% |
| Country concentration | 30% |

```text
Concentration Risk Score =
40% Holdings-Count Risk
+ 30% Sector Concentration Score
+ 30% Country Concentration Score
```

Where a concentration measure is not applicable, the available weights are automatically rebalanced.

For example, standard sector concentration is not applied to bond or gold ETFs.

## 10. Overall Risk Score

The final score combines three dimensions:

| Risk dimension | Weight |
|---|---:|
| Market risk | 60% |
| Concentration risk | 30% |
| Currency risk | 10% |

```text
Overall Risk Score =
60% Market Risk Score
+ 30% Concentration Risk Score
+ 10% Currency Risk Score
```

All 20 ETFs receive an overall score from 0 to 100.

## 11. Risk Bands

Overall scores were assigned to five risk bands:

| Score | Risk band |
|---:|---|
| 0–20 | Very Low |
| Above 20–40 | Low |
| Above 40–60 | Moderate |
| Above 60–80 | High |
| Above 80–100 | Very High |

The bands provide a simplified interpretation of the numerical scores.

## 12. Main Risk Driver

Each ETF is assigned a main risk driver based on its highest sub-score:

- Market risk
- Concentration risk
- Currency risk

This improves the explainability of the model by showing why an ETF receives its overall score.

## 13. Out-of-Sample Validation

The historical price period was divided into:

- Training period: July 2021 to July 2024
- Testing period: July 2024 to July 2026

The market-risk score was calculated using only training-period data.

It was then compared with three realised testing-period outcomes:

- Future annualised volatility
- Future maximum drawdown
- Future CVaR

### Validation results

| Future outcome | Pearson correlation | Spearman correlation |
|---|---:|---:|
| Volatility | 0.758 | 0.689 |
| Maximum drawdown | 0.734 | 0.687 |
| CVaR | 0.807 | 0.696 |

All six relationships were statistically significant at the 5% level.

The strongest relationship was between the training-period risk score and future CVaR.

These results provide evidence that ETFs receiving higher risk scores generally experienced worse future downside outcomes.

However, the findings should be treated as supporting evidence rather than proof of predictive performance because the sample contains only 20 ETFs.

## 14. Sensitivity Analysis

The model was tested under four market-risk weighting scenarios:

- Base model
- Volatility-focused
- Downside-focused
- Equal weighting

Most ETFs moved by no more than one to three ranking positions.

`VGOV.L` was the most sensitive ETF and moved by up to five positions.

The results suggest that the rankings are broadly stable under reasonable alternative weighting choices.

## 15. Reproducibility

The analysis is organised into numbered notebooks:

1. Data collection
2. Data cleaning
3. Market-risk metrics
4. Holdings metrics
5. Exposure metrics
6. Risk scoring
7. Model validation
8. Visual outputs

The notebooks should be run in numerical order.

Processed outputs are stored in:

```text
data/processed/
```

Charts are stored in:

```text
outputs/figures/
```

The Streamlit dashboard is stored in:

```text
dashboard/app.py
```

## 16. Interpretation

The framework is designed as a comparative risk-assessment tool.

It does not predict the precise amount an investor will gain or lose.

A score of zero does not mean that an ETF is risk-free. It means that the ETF has the lowest relative score within the selected sample.

Similarly, a score of 100 identifies the highest relative score within the selected sample rather than the maximum possible investment risk.

## 17. Disclaimer

The framework is for academic and educational purposes only.

It does not constitute financial advice.
