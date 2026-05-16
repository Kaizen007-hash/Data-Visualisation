from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def load_dataset(csv_path: Path) -> pd.DataFrame:
    if csv_path.exists():
        return pd.read_csv(csv_path)

    print(f"Warning: {csv_path} not found. Using sample dataset instead.")
    return pd.DataFrame(
        {
            "Date": pd.date_range("2025-01-01", periods=10, freq="D").strftime("%Y-%m-%d"),
            "T1": np.linspace(0.0, 1.0, 10),
            "T2": np.linspace(1.0, 2.0, 10),
        }
    )


def summarize_dataset(df: pd.DataFrame) -> None:
    print("Dataset summary")
    print("-----------------")
    print(df.info())
    print()
    print(df.head(5).to_string(index=False))
    print()

    numeric_df = df.select_dtypes(include="number")
    if not numeric_df.empty:
        print("Numeric summary")
        print("---------------")
        print(numeric_df.describe().to_string())


def fibonacci_sequence(n: int) -> list[int]:
    if n < 2:
        raise ValueError("The Fibonacci length must be at least 2.")

    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


def plot_fibonacci(sequence: list[int]) -> None:
    plt.figure(figsize=(10, 5))
    plt.plot(sequence, marker="o", linestyle="-", color="tab:blue")
    plt.title("Fibonacci Sequence")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.grid(True)
    plt.yscale("log")
    plt.tight_layout()
    plt.show()


def plot_dataset(df: pd.DataFrame, save_dir: Path | None = None) -> None:
    numeric_columns = list(df.select_dtypes(include="number").columns)
    if len(numeric_columns) < 2:
        print("Skipping dataset plots: at least two numeric columns are required.")
        return

    x_col, y_col = numeric_columns[:2]
    figures: list[tuple[str, plt.Figure]] = []

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.scatter(df[x_col], df[y_col], alpha=0.7, color="tab:blue", edgecolor="white", linewidth=0.4)
    ax.set_title(f"{x_col} vs {y_col}")
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.grid(True, alpha=0.3)
    figures.append(("scatter", fig))

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    for ax, col in zip(axes, [x_col, y_col]):
        ax.hist(df[col].dropna(), bins=30, color="tab:green", edgecolor="black", alpha=0.8)
        ax.set_title(f"{col} Distribution")
        ax.set_xlabel(col)
        ax.set_ylabel("Frequency")
        ax.grid(True, alpha=0.3)
    fig.tight_layout()
    figures.append(("histograms", fig))

    if save_dir is not None:
        save_dir.mkdir(parents=True, exist_ok=True)
        for name, fig in figures:
            output_path = save_dir / f"{name}.png"
            fig.savefig(output_path, dpi=150, bbox_inches="tight")
            print(f"Saved {output_path}")

    plt.show()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Load a CSV dataset, print a summary, and generate quick plots.")
    parser.add_argument("--csv", type=Path, default=Path("DA_1.csv"), help="Path to the input CSV file")
    parser.add_argument("--fib", type=int, default=20, help="Number of Fibonacci values to plot")
    parser.add_argument("--dataset-plots", action="store_true", help="Plot scatter and histogram charts for numeric columns")
    parser.add_argument("--save-dir", type=Path, help="Optional folder for saving generated dataset plots")
    parser.add_argument("--no-plot", action="store_true", help="Skip plotting the Fibonacci sequence")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    df = load_dataset(args.csv)
    summarize_dataset(df)

    if not args.no_plot:
        fib_sequence = fibonacci_sequence(args.fib)
        plot_fibonacci(fib_sequence)

    if args.dataset_plots:
        plot_dataset(df, args.save_dir)


if __name__ == "__main__":
    main()
