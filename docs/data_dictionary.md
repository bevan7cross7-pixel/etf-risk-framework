# Data Dictionary

This document explains the main datasets and variables used in the ETF Risk Framework.

## 1. ETF Master Dataset

File:

```text
data/processed/etf_universe_clean.csv
```

| Column | Description |
|---|---|
| `ETF_ID` | Short identifier used for the ETF, such as `VWRP` or `VUAG`. |
| `ETF_Name` | Full name of the ETF. |
| `Ticker` | Market ticker used to download historical price data. |
| `Provider` | ETF provider, such as Vanguard, iShares or Invesco. |
| `Risk_Category` | Initial descriptive risk category included in the source dataset. |
| `Asset_Class` | Main asset class, such as Equity, Bond, Gold or Property. |
| `Region` | Main geographical focus of the ETF. |
| `Sector_Focus` | Broad or specialist sector focus. |
| `Number_of_Holdings` | Number of securities or assets held by the ETF. |
| `Holdings_Data_Quality` | Classification describing the quality of the holdings information. |
| `Main_Currency_Exposure` | Main currency or group of currencies represented by the ETF. |
| `Currency_Risk_Level` | Simplified currency-risk category: Low, Medium or High. |
| `Data_As_Of` | Date associated with the holdings or exposure information. |
| `Source_URL` | URL of the provider or index source. |
| `Notes` | Assumptions, corrections, proxies or other relevant information. |

## 2. Clean Historical Prices

File:

```text
data/processed/etf_prices_clean.csv
```

| Column | Description |
|---|---|
| `Date` | Trading date. |
| ETF ticker columns | Adjusted daily closing price for each ETF. |

Small missing-value gaps were forward-filled to align trading dates across different exchanges.

## 3. Market-Risk Metrics

File:

```text
data/processed/etf_risk_metrics.csv
```

| Column | Description |
|---|---|
| `ETF_ID` | Short ETF identifier. |
| `ETF_Name` | Full ETF name. |
| `Ticker` | Trading ticker. |
| `Provider` | ETF provider. |
| `Risk_Category` | Original descriptive risk category. |
| `Asset_Class` | Main ETF asset class. |
| `Annualised_Volatility` | Annualised standard deviation of daily returns, stored as a decimal. |
| `Maximum_Drawdown` | Largest historical decline from a previous peak, stored as a negative decimal. |
| `Daily_VaR_95` | Historical 95% daily Value at Risk return threshold. |
| `Daily_CVaR_95` | Average return during the worst 5% of trading days. |
| `Beta` | Sensitivity to `VWRP.L`, which is used as the market benchmark. |
| `Annualised_Volatility_Percent` | Annualised volatility displayed as a percentage. |
| `Maximum_Drawdown_Percent` | Maximum drawdown displayed as a percentage. |
| `Daily_VaR_95_Percent` | Daily VaR displayed as a positive loss percentage. |
| `Daily_CVaR_95_Percent` | Daily CVaR displayed as a positive loss percentage. |

## 4. Holdings Metrics

File:

```text
data/processed/etf_holdings_metrics_base.csv
```

| Column | Description |
|---|---|
| `ETF_ID` | Short ETF identifier. |
| `ETF_Name` | Full ETF name. |
| `Ticker` | Trading ticker. |
| `Asset_Class` | Main ETF asset class. |
| `Number_of_Holdings` | Number of securities or assets held by the ETF. |
| `Holdings_Count_Risk` | Normalised 0–100 diversification-risk proxy based on the logarithm of holdings count. |
| `Main_Currency_Exposure` | Main currency exposure. |
| `Currency_Risk_Level` | Low, Medium or High currency-risk category. |
| `Currency_Risk_Score` | Numeric currency-risk score: Low = 25, Medium = 50 and High = 75. |

A higher `Holdings_Count_Risk` means the ETF has fewer holdings relative to the other ETFs in the sample.

## 5. Sector Exposure

File:

```text
data/processed/etf_sector_exposure.csv
```

| Column | Description |
|---|---|
| `ETF_ID` | Short ETF identifier. |
| `ETF_Name` | Full ETF name. |
| `Ticker` | Trading ticker. |
| `Asset_Class` | Main asset class. |
| `Sector` | Sector or industry category. |
| `Weight (%)` | Percentage of the ETF allocated to the sector. |
| `Source_Quality` | Description of whether the value is exact provider data, index data or a proxy. |
| `Data_As_Of` | Date of the sector allocation. |
| `Source_URL` | Source used for the allocation. |
| `Notes` | Additional assumptions or limitations. |

Sector exposure is included for the 12 applicable equity ETFs.

## 6. Country Exposure

File:

```text
data/processed/etf_country_exposure.csv
```

| Column | Description |
|---|---|
| `ETF_ID` | Short ETF identifier. |
| `ETF_Name` | Full ETF name. |
| `Ticker` | Trading ticker. |
| `Asset_Class` | Main asset class. |
| `Country / Geography` | Country, region or geographical proxy. |
| `Weight (%)` | Percentage allocated to the country or region. |
| `Source_Quality` | Description of whether the value is exact data or a proxy. |
| `Data_As_Of` | Date of the geographical allocation. |
| `Source_URL` | Source used for the allocation. |
| `Notes` | Assumptions or limitations associated with the figure. |

Country exposure is included for 19 ETFs.

`SGLN.L` is excluded because physical gold does not have a conventional country allocation.

## 7. Sector Concentration

File:

```text
data/processed/etf_sector_concentration.csv
```

| Column | Description |
|---|---|
| `Ticker` | ETF trading ticker. |
| `Total_Weight` | Sum of all reported sector weights. |
| `Largest_Exposure` | Largest individual sector allocation. |
| `Number_of_Categories` | Number of reported sectors. |
| `HHI` | Sector Herfindahl–Hirschman Index. |
| `Effective_Categories` | Effective number of equally weighted sectors, calculated as `1 / HHI`. |

Higher HHI values indicate greater sector concentration.

## 8. Country Concentration

File:

```text
data/processed/etf_country_concentration.csv
```

| Column | Description |
|---|---|
| `Ticker` | ETF trading ticker. |
| `Total_Weight` | Sum of all reported country or geography weights. |
| `Largest_Exposure` | Largest individual geographical allocation. |
| `Number_of_Categories` | Number of reported countries or regions. |
| `HHI` | Country Herfindahl–Hirschman Index. |
| `Effective_Categories` | Effective number of equally weighted countries, calculated as `1 / HHI`. |

Higher HHI values indicate greater geographical concentration.

## 9. Full Scoring Components

File:

```text
data/processed/etf_scoring_components.csv
```

This file contains the complete set of raw measures, normalised scores, sub-scores and final outputs used by the model.

### Raw market-risk variables

| Column | Description |
|---|---|
| `Annualised_Volatility` | Annualised historical volatility. |
| `Maximum_Drawdown` | Largest historical peak-to-trough decline. |
| `Daily_VaR_95` | 95% historical Value at Risk. |
| `Daily_CVaR_95` | Average loss during the worst 5% of trading days. |
| `Beta` | Market sensitivity relative to `VWRP.L`. |
| `Drawdown_Risk_Value` | Absolute value of maximum drawdown. |
| `CVaR_Risk_Value` | Absolute value of CVaR. |
| `Beta_Risk_Value` | Beta after negative values are clipped to zero. |

### Normalised metric scores

| Column | Description |
|---|---|
| `Volatility_Score` | Min-max normalised volatility score from 0 to 100. |
| `Drawdown_Score` | Min-max normalised drawdown score from 0 to 100. |
| `CVaR_Score` | Min-max normalised CVaR score from 0 to 100. |
| `Beta_Score` | Min-max normalised beta score from 0 to 100. |
| `Sector_Concentration_Score` | Normalised sector HHI score. |
| `Country_Concentration_Score` | Normalised country HHI score. |
| `Holdings_Count_Risk` | Normalised holdings-count risk score. |
| `Currency_Risk_Score` | Numeric currency-risk category score. |

### Model sub-scores and outputs

| Column | Description |
|---|---|
| `Market_Risk_Score` | Weighted combination of volatility, drawdown, CVaR and beta. |
| `Concentration_Risk_Score` | Weighted combination of holdings, sector and country concentration. |
| `Overall_Risk_Score` | Final weighted risk score from 0 to 100. |
| `Risk_Rank` | ETF position when scores are ranked from highest to lowest risk. |
| `Risk_Band` | Very Low, Low, Moderate, High or Very High. |
| `Main_Risk_Driver` | Highest of the market, concentration or currency sub-scores. |

## 10. ETF Risk Ranking

File:

```text
data/processed/etf_risk_ranking.csv
```

| Column | Description |
|---|---|
| `Risk_Rank` | Position from highest to lowest overall risk. |
| `ETF_ID` | Short ETF identifier. |
| `ETF_Name` | Full ETF name. |
| `Ticker` | Trading ticker. |
| `Asset_Class` | Main ETF asset class. |
| `Market_Risk_Score` | Market-risk sub-score. |
| `Concentration_Risk_Score` | Concentration-risk sub-score. |
| `Currency_Risk_Score` | Currency-risk sub-score. |
| `Overall_Risk_Score` | Final comparative 0–100 risk score. |
| `Risk_Band` | Simplified risk classification. |
| `Main_Risk_Driver` | Main source of risk identified by the model. |

## 11. Out-of-Sample Validation

File:

```text
data/processed/out_of_sample_validation.csv
```

| Column | Description |
|---|---|
| `Ticker` | ETF trading ticker. |
| `Training_Market_Risk_Score` | Market-risk score calculated using the training period. |
| `Testing_Volatility` | Realised annualised volatility during the later testing period. |
| `Testing_Max_Drawdown` | Realised maximum drawdown during the testing period. |
| `Testing_CVaR` | Realised CVaR during the testing period. |

## 12. Validation Significance

File:

```text
data/processed/validation_significance.csv
```

| Column | Description |
|---|---|
| `Outcome` | Future realised risk measure being tested. |
| `Pearson_Correlation` | Linear correlation between the training score and future outcome. |
| `Pearson_P_Value` | Statistical significance of the Pearson correlation. |
| `Spearman_Correlation` | Rank correlation between the training score and future outcome. |
| `Spearman_P_Value` | Statistical significance of the Spearman correlation. |

## 13. Sensitivity Analysis Files

### `sensitivity_scores.csv`

Contains the risk scores produced under each alternative weighting scenario.

### `sensitivity_rankings.csv`

Contains the ETF rankings under each scenario.

### `sensitivity_rank_correlations.csv`

Contains Spearman rank correlations between the alternative scenarios.

### `sensitivity_summary.csv`

Contains the average and maximum absolute ranking movement under each scenario.

### `sensitivity_rank_changes.csv`

Shows how many positions each ETF moved relative to the base model.

## 14. Missing Values

Some missing values are intentional because particular measures are not applicable.

Examples include:

- Sector concentration is not used for bond, gold or property ETFs.
- Country concentration is not used for physical gold.
- Missing non-applicable measures are excluded and the remaining concentration weights are rebalanced.

Missing values should therefore not automatically be interpreted as data-quality errors.

## 15. Units and Conventions

- Raw return and risk variables are generally stored as decimals.
- Columns containing `Percent` or `Weight (%)` are stored as percentage values.
- Risk scores range from 0 to 100.
- Higher scores indicate greater comparative risk.
- Dates use the `YYYY-MM-DD` format where possible.
- A risk score of zero means the lowest relative score in the sample, not zero investment risk.