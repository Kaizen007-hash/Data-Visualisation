# Data Visualisation

This repository contains Jupyter notebooks and CSV datasets for practicing data visualisation, exploratory data analysis, sensor analytics, filtering, regression, and simple forecasting workflows.

## Project Contents

| File | Description |
| --- | --- |
| `Data Visualization Practice.ipynb` | General visualisation practice using `DA_1.csv`. Covers Pandas loading, Matplotlib and Seaborn plots, Plotly charts, polynomial regression, sigmoid filtering, Kalman filtering, and scikit-learn forecasting. |
| `IoT Sensor_Data Project Day 1.ipynb` | Initial IoT sensor data exploration across daily CSV files, including data loading, cleaning, feature engineering, and trend visualisation. |
| `IoT Sensor Data Analysis & Forecasting.ipynb` | IoT sensor analysis notebook focused on exploratory analysis, correlation review, pattern identification, moving averages, and forecasting-oriented visualisation. |
| `IoT Combined_Sensor_Data.ipynb` | Combined workflow for loading multiple IoT sensor CSV files and analysing the joined sensor dataset. |
| `DA_1.csv` | Practice dataset with `Date`, `T1`, and `T2` columns. |
| `sensor_data_2025-03-01.csv` to `sensor_data_2025-03-07.csv` | Daily IoT sensor readings sampled every 5 seconds, including temperature, humidity, light, pH, and electrical conductivity. |

## Data Summary

`DA_1.csv` contains 3,145 rows and 3 columns:

- `Date`
- `T1`
- `T2`

Each daily IoT CSV contains 17,280 rows and 6 columns:

- `timestamp`
- `temperature`
- `humidity`
- `light`
- `pH`
- `electrical_conductivity`

## Main Techniques Used

- Data loading and cleaning with Pandas
- Numerical operations with NumPy
- Static plotting with Matplotlib and Seaborn
- Interactive visualisation with Plotly
- Correlation analysis and statistical summaries
- Moving averages and feature engineering
- Polynomial regression with scikit-learn
- Sigmoid filtering and smoothing
- Kalman filtering with `pykalman`
- Rolling-window forecasting with scikit-learn

## Setup

Install the required Python packages:

```bash
python -m pip install pandas numpy matplotlib seaborn plotly scikit-learn scipy pykalman nbformat nbclient ipykernel
```

If you are installing from inside a Jupyter notebook, use:

```python
%pip install pandas numpy matplotlib seaborn plotly scikit-learn scipy pykalman nbformat nbclient ipykernel
```

## Running The Notebooks

1. Open the folder in Jupyter Notebook, JupyterLab, VS Code, or another notebook environment.
2. Start with `Data Visualization Practice.ipynb` for the general visualisation workflow.
3. Use the IoT notebooks for the multi-day sensor datasets.
4. Make sure the CSV files stay in the same folder as the notebooks, because the notebooks read them using relative paths.

## Notes

TensorFlow was not required for the final working version of `Data Visualization Practice.ipynb`. The forecasting cells were adjusted to use scikit-learn so the notebook can run reliably in the current Python environment.
