# Reproducibility Instructions

## 1. Clone the Repository

```bash
git clone https://github.com/bevan7cross7-pixel/etf-risk-framework.git
cd etf-risk-framework
```

## 2. Install the Required Packages

```bash
pip install -r requirements.txt
```

## 3. Required Raw Data

The following raw files are stored locally and are not included in the public GitHub repository:

```text
data/raw/ETF_Risk_Dataset.xlsx
data/raw/ETF_Risk_Exposure_Workbook.xlsx
data/raw/etf_prices_5y.csv
```

These files are excluded because the raw-data folder is listed in `.gitignore`.

## 4. Run the Notebooks

The notebooks should be run in this order:

```text
01_data_collection.ipynb
02_data_clean folder is listed in `.gitignore`.

## 4.ing.ipynb
03_risk_metrics.ipynb
04_holdings_metrics.ipynb
05_exposure_metrics.ipynb
06_risk_scoring.ipynb
07_model_validation.ipynb
08_visual_outputs.ipynb
```

Each notebook creates files needed by the next stage.

## 5. Notebook Outputs

Processed datasets are saved in:

```text
data/processed/
```

Charts are saved in:

```text
outputs/figures/
```

## 6. Run the Dashboard

From the main project folder, run:

```bash
python -m streamlit run dashboard/app.py
```

The dashboard will open in a web browser.

## 7. Updating the Analysis

Historical prices and ETF exposures change over time.

Before updating the model:

1. Refresh the historical price data.
2. Update holdings counts.
3. Update sector and country exposure data.
4. Check all exposure weights total approximately 100%.
5. Run the notebooks again in numerical order.

## 8. Important Notes

- The model compares risk within the selected 20-ETF sample.
- Some specialist and bond exposures use documented proxies.
- A score of 0 means lowest risk within the sample, not no investment risk.
- The project is for academic and educational purposes only.