# Literature Review

*Project: Investing ETF Risk Framework: A Holdings-Based Risk Scoring Model*

## 1. Introduction

This literature review examines existing research on the risk factors that influence the performance and risk profile of exchange-traded funds (ETFs). Understanding these risk factors is important because ETFs can be affected by wider market movements, as well as by the specific countries, sectors, industries, asset classes and currencies they are exposed to. By identifying the most relevant risk factors, this review provides the academic and practical justification for developing a multi-dimensional ETF risk framework.

Traditional investment risk measures often focus mainly on historical volatility or market beta. These measures are useful because they show how much an investment moves and how sensitive it is to the wider market. However, ETFs can differ significantly in terms of holdings concentration, asset class exposure, sector allocation, country exposure, liquidity, downside risk, tracking quality and investor suitability. Therefore, ETF risk should not be assessed through one measure alone. This review considers both traditional financial risk theory and ETF-specific research to identify the factors most relevant for assessing ETF risk in a transparent and explainable way.

The review is organised around the main dimensions that will inform the proposed scoring model: portfolio theory and diversification, market risk, downside and tail risk, holdings-based concentration risk, exposure-based risk, ETF-specific risks, investor risk profiles, and existing risk indicators. Together, these areas provide the basis for a framework that combines price-based, holdings-based and exposure-based measures into an overall ETF risk score and supporting risk-driver breakdown.

## 2. Portfolio Theory and Diversification

Portfolio theory provides the starting point for understanding why diversification matters when assessing ETF risk. Markowitz (1952) argues that investors should not assess assets in isolation but should consider how each investment contributes to the overall risk and return of a portfolio. This is relevant to ETFs because they are often viewed as naturally diversified products, even though the actual level of diversification can vary significantly depending on the ETF’s underlying holdings.

For example, a broad global equity ETF may invest in thousands of companies across different countries and sectors, while a technology-focused ETF may be heavily concentrated in a smaller number of companies within one industry. Although both products are ETFs, their risk profiles may therefore be very different. This shows that ETF diversification depends not only on the product label, but also on what the fund actually holds and how those holdings are weighted.

Diversification literature also shows that the risk-reducing benefits of diversification depend on more than simply the number of assets held. Woerheide and Persson (1993) argue that counting the number of holdings can be misleading because portfolios are rarely equally weighted. This means an ETF with many holdings may still be highly concentrated if a small number of companies make up a large proportion of the fund. As a result, holdings-based measures such as top-ten holdings weight, sector concentration, country concentration and the Herfindahl-Hirschman Index can help identify whether an ETF is genuinely diversified or exposed to hidden concentration risk. This supports the use of holdings data alongside price data in the proposed ETF risk framework.

## 3. Market Risk: Volatility and Beta

While portfolio theory explains the importance of diversification, traditional finance literature also focuses heavily on market risk. Market risk refers to the possibility that an investment may lose value due to movements in the wider market. It is commonly measured through volatility and beta. Volatility measures how much an asset’s returns fluctuate over time, while beta measures the sensitivity of an asset or fund to movements in a wider market benchmark.

Sharpe’s (1964) Capital Asset Pricing Model introduced beta as a key measure of systematic risk, suggesting that investors should be compensated for the level of market risk they are exposed to. This is relevant to ETF risk assessment because different ETFs can respond very differently to market movements depending on their underlying assets. For example, an S&P 500 ETF is likely to move closely with the US equity market, while a government bond ETF may behave differently during periods of equity market stress.

Volatility is also widely used in market risk management because it provides a simple and comparable measure of return variation. The RiskMetrics framework developed by J.P. Morgan and Reuters (1996) helped popularise the use of volatility and correlation in financial risk measurement, particularly through approaches such as Value at Risk. This supports the inclusion of price-based risk measures in the ETF risk framework, as historical returns can show how unstable or sensitive an ETF has been over time.

However, volatility and beta should not be treated as complete measures of ETF risk. Fama and French (1992) questioned the strength of beta as the only explanation of expected returns, arguing that other factors can also help explain differences in asset performance. In an ETF context, two funds may have similar volatility or beta but very different holdings concentration, sector exposure, country exposure or downside risk. ETF-specific research also suggests that market risk should be considered alongside other risk dimensions. Ben-David, Franzoni and Moussawi (2018) find that ETFs can influence the volatility of their underlying securities, suggesting that ETF risk may come not only from the assets held, but also from the way ETFs are traded in the market. Therefore, volatility and beta are useful starting points, but they should form only one part of a wider multi-dimensional framework.

## 4. Downside Risk and Tail Risk

Market risk measures are useful, but investors are often more concerned with losses than general price movement. Traditional volatility measures both positive and negative changes in returns, meaning it does not fully distinguish between upside movements and harmful downside movements. As a result, volatility alone may not reflect the type of risk that matters most to investors. Sortino and Price (1994) argue that downside risk provides a more relevant view of investment risk because it focuses specifically on returns falling below a target or acceptable level.

Maximum drawdown is one way to measure downside risk because it shows the largest fall in value from a previous peak to a later trough. This makes it useful in a practical ETF framework because it is easy to understand and clearly shows how much an investor could have lost during a difficult period. Chekhlov, Uryasev and Zabarankin (2005) explain that drawdown measures are useful in portfolio risk management because they focus on the decline in portfolio value over time, rather than only short-term return variation. For ETFs, this is relevant because higher-risk areas such as emerging markets, clean energy or technology may experience deeper drawdowns than broad developed-market equity ETFs or government bond ETFs.

Tail risk measures are also important because they focus on extreme losses that may occur during unusual or stressed market conditions. Value at Risk estimates the maximum expected loss over a given time period at a chosen confidence level, and RiskMetrics helped popularise this type of market risk measurement (J.P. Morgan and Reuters, 1996). However, Value at Risk has limitations because it identifies a loss threshold but does not explain how severe losses may be beyond that threshold. Artzner et al. (1999) criticise some traditional risk measures and argue for coherent risk measures that better capture financial risk. Conditional Value at Risk, also known as Expected Shortfall, addresses this limitation by estimating the average loss in the worst-performing outcomes. Rockafellar and Uryasev (2000) show that Conditional Value at Risk is useful because it captures losses beyond the Value at Risk cut-off, making it more informative for understanding extreme downside outcomes.

Including downside and tail risk measures supports the development of a multi-dimensional ETF risk framework because it helps explain risks that volatility and beta may not fully capture. Two ETFs may have similar average returns or volatility, but one may suffer much larger losses during market stress. By including maximum drawdown, Value at Risk and Conditional Value at Risk, the framework can provide a clearer risk-driver breakdown and help users understand not only how much an ETF moves, but how badly it may fall during negative market conditions.

## 5. Holdings-Based Concentration Risk

The previous sections show why price behaviour matters, but they do not fully explain where ETF risk comes from. Holdings-based concentration risk is important because the name or category of an ETF does not always show the true level of risk inside the fund. ETFs are often seen as diversified investments, but their actual risk depends on the assets they hold and how much weight is placed on each holding. Therefore, an ETF should not be judged only by the number of holdings it contains, but also by how those holdings are distributed.

This is important because two ETFs may appear similar but have very different levels of concentration. A broad global equity ETF may hold thousands of companies across different countries and sectors, while a sector-focused ETF, such as a technology or clean energy ETF, may be heavily exposed to a smaller number of companies or industries. Even broad market-cap weighted ETFs can become concentrated if a small number of large companies make up a high percentage of the index. This means an ETF can appear diversified on the surface while still being highly dependent on a limited number of stocks, sectors or countries.

Concentration risk can be measured using holdings-based metrics such as the percentage weight of the top ten holdings, sector concentration, country concentration, the Herfindahl-Hirschman Index and the effective number of holdings. Woerheide and Persson (1993) support the use of weighted concentration measures because portfolio weights are not usually equal. Kacperczyk, Sialm and Zheng (2005) also show that industry concentration is an important characteristic of fund portfolios, which supports the idea that sector exposure should be considered when assessing risk.

ETF-specific research further supports the use of underlying holdings data. Kakushadze and Yu (2022) argue that ETF risk models can be developed using ETF classifications and constituent data, showing that the underlying structure of an ETF is important for identifying its risk factors. FINRA (2022) similarly advises investors to examine fund holdings to identify concentration risk. This is relevant to the proposed framework because holdings data can reveal the real sources of ETF risk, including company concentration, sector exposure and regional exposure. As a result, holdings-based concentration measures provide a more explainable approach than relying only on price-based measures such as volatility or beta.

## 6. Exposure-Based Risk: Sector, Country, Asset Class and Currency

Holdings concentration is one part of a wider issue: ETF risk is also shaped by the exposures that the fund provides. Exposure-based risk refers to the risks created by the asset classes, sectors, countries and currencies an ETF is exposed to. ETFs can provide exposure to global equities, developed market equities, emerging markets, government bonds, corporate bonds, high-yield bonds, gold, property and specific sectors such as technology, healthcare or clean energy. Each of these exposures has a different risk profile, meaning ETFs should not be compared only as one general investment category. Brinson, Hood and Beebower (1986) show that asset allocation is a major driver of portfolio performance, which supports the idea that the asset class exposure of an ETF is an important factor when assessing risk.

The asset class of an ETF can significantly affect its risk level. Equity ETFs are generally more exposed to stock market movements, while bond ETFs are more affected by interest rate risk, credit risk and duration risk. Government bond ETFs are often considered lower risk because they are backed by government debt, whereas corporate bond ETFs introduce additional credit risk. High-yield bond ETFs are usually riskier than investment-grade corporate bond ETFs because they hold debt issued by companies with lower credit ratings and a higher probability of default. Elton et al. (2001) show that corporate bond spreads are influenced by expected default losses and risk premiums, which supports the inclusion of bond type and credit quality within an ETF risk framework.

Sector and industry exposure also play an important role in ETF risk. A broad global equity ETF may spread investments across many sectors, while a sector ETF may be concentrated in one area of the market. For example, technology and clean energy ETFs may offer higher growth potential, but they can also be more vulnerable to sector-specific shocks, valuation changes and changes in investor sentiment. Kacperczyk, Sialm and Zheng (2005) show that industry concentration is an important characteristic of fund portfolios, which supports the idea that sector exposure should be measured when assessing ETF risk.

Country and regional exposure are also important because ETFs investing in different markets can face different economic, political and regulatory risks. A UK equity ETF, US equity ETF, Japan ETF and emerging markets ETF may all respond differently to changes in inflation, interest rates, exchange rates, government policy and economic growth. Bekaert and Harvey (1995) show that emerging markets can have different levels of integration with global markets, which means their risk and return behaviour may differ from developed markets. This supports the inclusion of country and regional exposure within the ETF risk framework, especially for ETFs focused on China, emerging markets or single-country indices.

Currency exposure is particularly relevant for UK investors because many ETFs available on UK platforms hold overseas assets. Even when an ETF is listed in pounds, the underlying holdings may be priced in foreign currencies such as US dollars, euros or yen. As a result, changes in exchange rates can affect the return that a UK investor receives. Campbell, Serfaty-de Medeiros and Viceira (2010) show that currency exposure can affect the risk of international equity and bond portfolios. Therefore, exposure-based risk should be included in the framework because it helps explain where an ETF’s risk comes from, whether through asset class, sector, country or currency exposure.

## 7. ETF-Specific Risks: Liquidity, Tracking and Structure

Even when the underlying exposures are understood, ETFs can still involve risks that are specific to the ETF structure itself. These include liquidity risk, bid-ask spread risk, tracking error, tracking difference and risks linked to the creation and redemption process. This means that ETF risk is not only determined by the underlying assets, but also by how efficiently the ETF trades and how closely it follows its benchmark.

Liquidity risk is particularly important because ETFs trade on exchanges like shares, meaning investors may face different trading costs depending on market conditions. During normal periods, many ETFs trade efficiently with narrow bid-ask spreads. However, during periods of market stress, liquidity can worsen and spreads may widen, making ETFs more expensive to buy or sell. IOSCO (2021) highlights that the March 2020 market stress created a more challenging liquidity environment for some ETFs. This is relevant because bond ETFs, high-yield bond ETFs, property ETFs and thematic ETFs may be more exposed to liquidity issues than broad, highly traded equity ETFs.

The creation and redemption process is also important to ETF structure. Authorised participants help keep ETF prices close to the value of the underlying assets by creating or redeeming ETF shares. However, this process may become more difficult during stressed market conditions if the underlying assets are less liquid. This is especially relevant for fixed income ETFs, where the ETF may trade more easily than the bonds it holds. Aquilina et al. (2020) find that fixed income ETF primary markets are highly concentrated, which supports the need to consider liquidity and resilience when assessing ETF risk.

Tracking risk is another ETF-specific issue. ETFs are expected to follow the performance of their benchmark index, but they may not do this perfectly. Tracking error measures the variation between ETF returns and benchmark returns, while tracking difference shows the actual performance gap between the ETF and the index over time. This can be caused by management fees, transaction costs, replication method, cash drag, sampling techniques and market conditions. As a result, two ETFs tracking similar markets may still produce different investor outcomes. Including tracking-related measures can therefore help identify whether an ETF is efficiently delivering the exposure it is designed to provide.

ETF-specific research also shows that ETFs can affect the underlying securities they hold. Ben-David, Franzoni and Moussawi (2018) find that stocks with higher ETF ownership can experience higher volatility, suggesting that ETF trading activity may transmit shocks into the underlying market. Similarly, Israeli, Lee and Sridharan (2017) argue that higher ETF ownership is associated with higher trading costs and lower pricing efficiency in underlying securities. These studies suggest that ETFs should not be viewed only as simple passive products, as their structure and trading activity can create additional risks.

Overall, ETF-specific risks should be included in the proposed framework because they help explain risks that are not captured by volatility, beta or holdings concentration alone. Liquidity indicators such as trading volume, bid-ask spread and assets under management can show how easily an ETF can be traded, while tracking error and tracking difference can show how effectively the ETF follows its benchmark. However, some of this data may be difficult to collect consistently across all ETFs, so these measures may need to be treated as secondary or contextual indicators rather than core scoring factors.

## 8. Investor Risk Profiles and Suitability

A risk framework should also recognise that risk is not experienced in the same way by every investor. Different investors have different levels of risk tolerance, investment objectives, financial knowledge and time horizons. For example, a younger investor with a long investment horizon may be more willing to accept short-term volatility if they are seeking higher long-term growth. In contrast, an older investor, or an investor with a shorter time horizon, may prefer lower-risk investments such as government bond ETFs or diversified aggregate bond ETFs. Droms and Strauss (2003) argue that asset allocation should consider both risk tolerance and time horizon, which supports the idea that ETF risk should be assessed in relation to different investor needs.

This is relevant to ETF selection because different ETF categories are designed to provide different types of exposure. Broad global equity ETFs and developed-market ETFs may suit investors looking for diversified long-term equity exposure, while emerging market ETFs, technology ETFs and clean energy ETFs may appeal to investors willing to accept higher volatility and concentration risk. Bond ETFs, such as government bond or global aggregate bond ETFs, may be more suitable for cautious investors or those seeking lower volatility. Alternative ETFs or exchange-traded commodities, such as gold and property products, may also be used by investors looking for diversification outside traditional equity and bond markets.

Investor suitability is also important from a regulatory and consumer understanding perspective. Grable and Lytton (1999) show that financial risk tolerance varies between individuals, which supports the idea that a single risk measure may not be suitable for all investors. The Financial Conduct Authority (2026) also highlights the importance of consumers understanding the risks and features of complex exchange-traded products before investing. In addition, The Investment Association (2025) reports that a significant proportion of UK retail investors have limited knowledge of ETFs and how to compare them. This supports the need for clearer ETF risk communication, especially because retail investors may not always understand how ETF structure, exposure or concentration affects risk.

This justifies the use of a balanced ETF sample covering lower-risk, medium-risk, higher-risk and alternative ETFs. Including government bonds, corporate bonds, global equities, developed-market equities, emerging markets, sector ETFs, gold and property allows the framework to compare ETFs across different investor preferences and risk profiles. However, the purpose of the framework is not to recommend specific ETFs or provide financial advice. Instead, it aims to explain the risk characteristics of different ETFs in a transparent way, helping users understand why one ETF may be considered higher or lower risk than another.

## 9. Existing Risk Indicators and the Research Gap

The literature also highlights a gap in how ETF risk is commonly communicated. Existing risk indicators provide a useful starting point for comparing investment products, but they may not fully explain why an ETF is risky. Regulatory documents, such as the Key Information Document used under the PRIIPs framework, use a Summary Risk Indicator to present investment risk on a simple scale. This can be helpful for retail investors because it gives a quick and standardised view of risk. However, this type of indicator often summarises risk into a single category, which may not clearly show the underlying causes of risk, such as holdings concentration, sector exposure, country exposure, currency exposure, drawdown risk, liquidity risk or tracking risk.

This creates a limitation when comparing ETFs. Two ETFs may receive similar risk ratings but have very different risk drivers. For example, one ETF may be risky because it is concentrated in technology stocks, while another may be risky because it invests in emerging markets or high-yield bonds. A single risk score may show that both products are higher risk, but it may not explain where the risk comes from. This is important because investors need to understand not only the level of risk, but also the source of that risk.

The Financial Conduct Authority’s Summary Risk Indicator guidance shows that risk indicators are designed to provide a simplified comparison of products, but the accompanying narrative must also explain relevant risks, including risks not fully captured by the indicator (Financial Conduct Authority, 2022). This supports the argument that a single score on its own may not be enough for clear ETF risk communication. Research on explainable financial modelling also supports this point. Bussmann et al. (2020) argue that explainability is important in financial risk models because users need to understand which variables influence a model’s output. This is relevant to the proposed ETF framework because the aim is not only to calculate a risk score, but also to show the key risk drivers behind that score.

Therefore, the research gap is the need for a more transparent and explainable ETF risk framework that combines multiple dimensions of risk. The proposed project addresses this gap by combining price-based risk measures, holdings-based concentration measures and exposure-based risk measures into a single 0-100 ETF risk score. In addition, the dashboard or scorecard will provide a breakdown of the main risk drivers, allowing users to understand why one ETF is rated as higher or lower risk than another. This improves on basic risk indicators by making the risk assessment more transparent, interpretable and useful for ETF comparison.

## 10. Conclusion

Overall, the literature shows that ETF risk cannot be fully understood through a single measure such as volatility or beta. Portfolio theory supports the importance of diversification, but also shows that diversification depends on how assets are combined and weighted. Market risk literature supports the use of volatility and beta, while downside and tail risk literature shows the importance of measuring losses through maximum drawdown, Value at Risk and Conditional Value at Risk. These price-based measures are useful, but they do not fully explain the source of risk inside an ETF.

Holdings-based and exposure-based research therefore provides an important foundation for the proposed framework. Measures such as top-ten holdings weight, HHI, sector concentration, country exposure, asset class exposure and currency exposure can help identify whether an ETF is genuinely diversified or dependent on a limited number of risk drivers. ETF-specific literature also shows that liquidity, tracking quality and ETF structure can affect investor outcomes, particularly during periods of market stress. Finally, investor suitability literature and regulatory guidance show that risk should be communicated clearly, as different investors have different levels of knowledge, risk tolerance and time horizons.

The main research gap identified is that existing ETF risk indicators are useful for providing a simple comparison, but they often do not explain why one ETF is riskier than another. This project responds to that gap by developing a multi-dimensional ETF risk framework that combines market risk, downside risk, holdings concentration, exposure risk and ETF-specific indicators into an explainable 0-100 scoring model. The proposed dashboard or scorecard will also show the main risk drivers behind each score, making the framework more transparent and practical for ETF comparison. This literature review therefore supports the development of a holdings-based ETF risk scoring model and provides justification for the factors selected within the framework.

## Conceptual Framework Summary

The literature reviewed above supports the following risk dimensions for the proposed ETF risk framework:

| Risk dimension | Metrics used | Literature support |
|---|---|---|
| Market risk | Volatility; beta | Sharpe (1964); J.P. Morgan and Reuters (1996) |
| Downside and tail risk | Maximum drawdown; VaR; CVaR | Sortino and Price (1994); Artzner et al. (1999); Rockafellar and Uryasev (2000) |
| Concentration risk | Top-ten weight; HHI; effective holdings | Markowitz (1952); Woerheide and Persson (1993); Kacperczyk et al. (2005) |
| Exposure risk | Asset class; sector; country; currency | Brinson et al. (1986); Bekaert and Harvey (1995); Campbell et al. (2010) |
| ETF-specific risk | Liquidity; bid-ask spread; AUM; tracking error | IOSCO (2021); Aquilina et al. (2020); Israeli et al. (2017) |
| Suitability and communication | Investor profile; risk category; dashboard risk drivers | Grable and Lytton (1999); Financial Conduct Authority (2026); Bussmann et al. (2020) |

## References

Aquilina, M., Croxson, K., Valentini, G.G. and Sun, Z. (2020) ‘Fixed income ETFs: primary market participation and resilience of liquidity during periods of stress’, *Economics Letters*, 193, 109279. doi: 10.1016/j.econlet.2020.109279.

Artzner, P., Delbaen, F., Eber, J.M. and Heath, D. (1999) ‘Coherent measures of risk’, *Mathematical Finance*, 9(3), pp. 203-228. doi: 10.1111/1467-9965.00068.

Bekaert, G. and Harvey, C.R. (1995) ‘Time-varying world market integration’, *The Journal of Finance*, 50(2), pp. 403-444. doi: 10.1111/j.1540-6261.1995.tb04790.x.

Ben-David, I., Franzoni, F. and Moussawi, R. (2018) ‘Do ETFs increase volatility?’, *The Journal of Finance*, 73(6), pp. 2471-2535. doi: 10.1111/jofi.12727.

Brinson, G.P., Hood, L.R. and Beebower, G.L. (1986) ‘Determinants of portfolio performance’, *Financial Analysts Journal*, 42(4), pp. 39-44. doi: 10.2469/faj.v42.n4.39.

Bussmann, N., Giudici, P., Marinelli, D. and Papenbrock, J. (2020) ‘Explainable AI in fintech risk management’, *Frontiers in Artificial Intelligence*, 3, Article 26. doi: 10.3389/frai.2020.00026.

Campbell, J.Y., Serfaty-de Medeiros, K. and Viceira, L.M. (2010) ‘Global currency hedging’, *The Journal of Finance*, 65(1), pp. 87-121. doi: 10.1111/j.1540-6261.2009.01524.x.

Chekhlov, A., Uryasev, S. and Zabarankin, M. (2005) ‘Drawdown measure in portfolio optimization’, *International Journal of Theoretical and Applied Finance*, 8(1), pp. 13-58. doi: 10.1142/S0219024905002767.

Droms, W.G. and Strauss, S.N. (2003) ‘Assessing risk tolerance for asset allocation’, *Journal of Financial Planning*, 16(3), pp. 72-77.

Elton, E.J., Gruber, M.J., Agrawal, D. and Mann, C. (2001) ‘Explaining the rate spread on corporate bonds’, *The Journal of Finance*, 56(1), pp. 247-277. doi: 10.1111/0022-1082.00324.

Fama, E.F. and French, K.R. (1992) ‘The cross-section of expected stock returns’, *The Journal of Finance*, 47(2), pp. 427-465. doi: 10.1111/j.1540-6261.1992.tb04398.x.

Financial Conduct Authority (2022) *Annex III: Presentation of the Summary Risk Indicator (SRI).* Available from: https://handbook.fca.org.uk/technical-standards/provision/s139c1216sn0p1809 [Accessed 12 June 2026].

Financial Conduct Authority (2026) *Complex exchange traded products - good practice and areas for improvement.* Available from: https://www.fca.org.uk/publications/good-and-poor-practice/complex-exchange-traded-products [Accessed 12 June 2026].

FINRA (2022) *Concentrate on concentration risk.* Available from: https://www.finra.org/investors/insights/concentration-risk [Accessed 12 June 2026].

Grable, J.E. and Lytton, R.H. (1999) ‘Financial risk tolerance revisited: The development of a risk assessment instrument’, *Financial Services Review*, 8(3), pp. 163-181. doi: 10.1016/S1057-0810(99)00041-4.

International Organization of Securities Commissions (2021) *Exchange Traded Funds Thematic Note: Findings and Observations during COVID-19 induced market stresses.* Available from: https://www.iosco.org/library/pubdocs/pdf/IOSCOPD682.pdf [Accessed 12 June 2026].

Israeli, D., Lee, C.M.C. and Sridharan, S.A. (2017) ‘Is there a dark side to exchange traded funds? An information perspective’, *Review of Accounting Studies*, 22(3), pp. 1048-1083. doi: 10.1007/s11142-017-9401-8.

J.P. Morgan and Reuters (1996) *RiskMetrics Technical Document.* 4th edn. Available from: https://www.msci.com/documents/10199/5915b101-4206-4ba0-aee2-3449d5c7e95a [Accessed 12 June 2026].

Kacperczyk, M., Sialm, C. and Zheng, L. (2005) ‘On the industry concentration of actively managed equity mutual funds’, *The Journal of Finance*, 60(4), pp. 1983-2011. doi: 10.1111/j.1540-6261.2005.00785.x.

Kakushadze, Z. and Yu, W. (2022) ‘ETF Risk Models’, *Bulletin of Applied Economics*, 9(1), pp. 1-17. Available from: https://arxiv.org/abs/2110.07138 [Accessed 12 June 2026].

Markowitz, H. (1952) ‘Portfolio selection’, *The Journal of Finance*, 7(1), pp. 77-91. doi: 10.2307/2975974.

Rockafellar, R.T. and Uryasev, S. (2000) ‘Optimization of conditional value-at-risk’, *Journal of Risk*, 2(3), pp. 21-41. doi: 10.21314/JOR.2000.038.

Sharpe, W.F. (1964) ‘Capital asset prices: A theory of market equilibrium under conditions of risk’, *The Journal of Finance*, 19(3), pp. 425-442. doi: 10.1111/j.1540-6261.1964.tb02865.x.

Sortino, F.A. and Price, L.N. (1994) ‘Performance measurement in a downside risk framework’, *The Journal of Investing*, 3(3), pp. 59-64. doi: 10.3905/joi.3.3.59.

The Investment Association (2025) *Retail Investors and ETFs.* Available from: https://www.theia.org/sites/default/files/2025-09/Retail%20Investors%20ETFs%20report_Final.pdf [Accessed 12 June 2026].

Woerheide, W. and Persson, D. (1993) ‘An index of portfolio diversification’, *Financial Services Review*, 2(2), pp. 73-85.