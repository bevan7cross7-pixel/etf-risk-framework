# Limitations

## 1. The Scores Are Comparative

The framework compares risk across the 20 ETFs included in the project.

A score of 0 does not mean that an ETF has no risk. It means that it has the lowest score within this group. A score of 100 means that it has the highest score within the group.

The scores would likely change if different ETFs were added or removed from the dataset.

## 2. Small ETF Sample

The project only includes 20 ETFs across chosen equities, bonds, gold and property.

This gives a useful range of ETFs, but it does not represent every ETF available to UK investors.

The validation results are also based on a small sample, so they should be treated as supporting evidence rather than proof that the model will always work in the future.

## 3. Historical Risk May Change

The market-risk measures are based on historical prices.

An ETF that had low volatility or drawdown in the past could become riskier in the future. Market conditions, interest rates and investor behaviour can all change over time.

The framework should therefore be used as a comparison tool rather than an exact prediction of future losses.

## 4. Different Data Sources

The holdings and exposure data came from different ETF providers and index providers.

These sources may:

- Use different sector categories
- Report data on different dates
- Round figures differently
- Classify countries differently
- Update their data at different times

This means some exposure data may not be completely consistent across every ETF.

## 5. Some Exposure Data Uses Proxies

Exact sector or country data was not available for every ETF.

Some bond, property and specialist ETF figures are based on:

- Index-level information
- The ETF's stated investment focus
- Top issuer locations
- Market or listing information

These values are clearly labelled in the `Source_Quality` and `Notes` columns.

They should be interpreted with more caution than exact data from an official provider.

## 6. Bond Country Exposure Is Difficult to Measure

Country exposure is not always straightforward for bond ETFs.

A bond could be classified by:

- The issuer's country
- The government that issued it
- The company's headquarters
- The bond's trading currency
- The country where the company is registered

These do not always represent the same type of exposure.

Because of this, some bond country-concentration results should be treated with caution.

## 7. Sector Risk Does Not Apply to Every ETF

Standard equity-sector data was not used for:

- Bond ETFs
- Physical gold
- Property ETFs

When a measure does not apply, it is removed and the remaining concentration weights are rebalanced.

This allows every ETF to receive a concentration score, but it also means that the score is not calculated using exactly the same measures for every asset class.

## 8. Currency Risk Is Simplified

Currency risk is grouped into three categories:

- Low
- Medium
- High

These are converted into scores of 25, 50 and 75.

This was done to make the method simple and easy to explain, but it does not directly measure:

- Exchange-rate volatility
- Currency correlations
- Currency hedging
- The investor's home currency
- The difference between trading currency and underlying currency exposure

The currency score should therefore be treated as a simple indicator rather than a complete currency-risk model.

## 9. Number of Holdings Does Not Show the Full Picture

The number of holdings is used as a simple diversification measure.

However, an ETF could hold hundreds of companies and still be heavily concentrated in a few large holdings, sectors or countries.

An ETF with fewer holdings could also be reasonably diversified if the weights are spread evenly.

For this reason, the holdings count is used alongside sector and country concentration.

## 10. Min-Max Normalisation Depends on the Sample

Each risk measure is converted to a score from 0 to 100 using min-max normalisation.

The ETF with the lowest value receives 0 and the ETF with the highest value receives 100.

This makes the results easy to compare, but extreme values can have a large effect on the scores.

The results are also dependent on the ETFs included in the sample.

## 11. The Weights Are a Modelling Choice

There is no single correct way to weight the risk measures.

The model uses:

- 60% market risk
- 30% concentration risk
- 10% currency risk

These weights were chosen based on the aims of the project and the supporting literature.

Sensitivity analysis was used to test different weighting choices. Most ETFs remained in a similar position, although `VGOV.L` moved by up to five places.

This shows that the model is broadly stable, but some ETFs are more sensitive to the selected weights.

## 12. VWRP.L Is Not a Perfect Benchmark for Every Asset Class

Beta is calculated using `VWRP.L` as the benchmark.

This works well as a broad global equity benchmark, but it is less suitable for bonds, gold and property.

A future version of the project could use separate benchmarks for different asset classes.

## 13. Missing Prices Were Forward-Filled

Small gaps in the price data were filled using the previous available price.

Most of these gaps were caused by different exchange holidays and trading calendars.

Forward-filling helps align the dates, but it assumes that the ETF price did not change during the missing day.

The number of missing observations was low, so the overall impact should be limited.

## 14. The Validation Mainly Tests Market Risk

The out-of-sample validation mainly tests the market-risk part of the framework.

Historical holdings, sector and country data were not available for the beginning of the training period.

This means the full final score could not be rebuilt using only information that was available before the testing period.

The validation therefore supports the market-risk part of the model, but it does not fully validate every part of the final score.

## 15. Correlation Does Not Prove Causation

The results showed that higher training-period risk scores were linked with worse future risk outcomes.

However, this does not mean that the score caused those outcomes.

It also does not guarantee that the same relationship will continue under different market conditions.

## 16. AI-Assisted Data Collection

Artificial intelligence was used to help locate, organise and structure some of the publicly available holdings and exposure data.

Official ETF-provider and index-provider sources were used where available.

Each exposure record includes:

- A source URL
- A data-as-of date
- A source-quality label
- Notes explaining any assumptions or proxies

AI-assisted data collection can still create transcription or classification errors. Important figures should therefore be checked against the original source before the framework is used outside this academic project.

## 17. ETF Data Changes Over Time

ETF holdings, sector allocations, country allocations and currency exposure can change as funds rebalance and markets move.

The dataset represents the latest available information at the recorded `Data_As_Of` dates.

The exposure data would need to be updated before repeating the analysis in the future.

## 18. Educational Purpose

The framework is for academic and educational use only.

It does not consider an investor's:

- Financial situation
- Investment goals
- Risk tolerance
- Tax position
- Investment time horizon
- Existing portfolio

The scores do not constitute financial advice.