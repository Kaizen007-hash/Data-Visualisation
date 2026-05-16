# Data Visualization Python Script

This repository contains a simple Python script to load a dataset, print a summary, and plot the Fibonacci sequence.

## Files

- `data_visualization.py`: The main Python script.
- `requirements.txt`: Required packages to run the script.

## Requirements

Install dependencies with:

```bash
python -m pip install -r requirements.txt
```

## Usage

Run the script with the default sample dataset or specify your own CSV file:

```bash
python data_visualization.py --csv DA_1.csv
```

Optional flags:

- `--fib`: Number of Fibonacci values to generate and plot (default: 20)
- `--no-plot`: Skip plotting the Fibonacci sequence

Example:

```bash
python data_visualization.py --csv DA_1.csv --fib 50
```

## Notes

If the file provided by `--csv` does not exist, the script will generate a sample dataset automatically.
