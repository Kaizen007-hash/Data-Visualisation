# Data Visualisation

This repository contains a Jupyter notebook, exported notebook results, generated figures, and a small Python utility script for practicing data visualisation with sensor-style numeric data.

## Repository Contents

| File | Description |
| --- | --- |
| `Data Visualization Practice.ipynb` | Main notebook with executed cells and visual outputs. |
| `Data Visualization Practice.md` | Markdown export of the notebook for quick reading on GitHub. |
| `DA_1.csv` | Practice dataset with `Date`, `T1`, and `T2` columns. |
| `data_visualization.py` | Command-line script for loading a CSV, printing summaries, plotting Fibonacci values, and creating quick dataset plots. |
| `output_*.png` | Notebook-generated plot images used by the Markdown export. |
| `requirements.txt` | Python packages needed for the notebook and script. |
| `.gitignore` | Ignore rules for local caches, virtual environments, and newly generated temporary output files. |

## Dataset

`DA_1.csv` contains 3,145 records with:

- `Date`
- `T1`
- `T2`

The notebook uses the dataset for exploratory data analysis, scatter plots, box plots, histograms, polynomial regression, sigmoid filtering, Kalman filtering, and simple forecasting examples.

## Setup

Create and activate a virtual environment if desired, then install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Inside Jupyter, use:

```python
%pip install -r requirements.txt
```

## Run The Notebook

Open `Data Visualization Practice.ipynb` in Jupyter Notebook, JupyterLab, or VS Code and run the cells from top to bottom.

The notebook has saved outputs, so GitHub can display the results even before rerunning it locally.

## Run The Script

Basic dataset summary plus Fibonacci plot:

```bash
python data_visualization.py --csv DA_1.csv
```

Generate dataset scatter and histogram plots:

```bash
python data_visualization.py --csv DA_1.csv --dataset-plots
```

Save generated dataset plots to a folder:

```bash
python data_visualization.py --csv DA_1.csv --dataset-plots --save-dir generated_plots
```

Useful options:

- `--csv`: path to the input CSV file
- `--fib`: number of Fibonacci values to plot
- `--dataset-plots`: generate quick numeric dataset plots
- `--save-dir`: save dataset plots as PNG files
- `--no-plot`: skip the Fibonacci plot

## Notes

- TensorFlow is not required for this project.
- The notebook depends on `plotly`, `scikit-learn`, `scipy`, `seaborn`, and `pykalman` in addition to the standard data stack.
- Existing `output_*.png` files are kept because the Markdown notebook export references them; newly generated output images are ignored by `.gitignore`.
