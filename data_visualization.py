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


def fibonacci_sequence(n: int) -> list[int]:
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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Load a CSV dataset, print summary, and display a Fibonacci plot.")
    parser.add_argument("--csv", type=Path, default=Path("DA_1.csv"), help="Path to the input CSV file")
    parser.add_argument("--fib", type=int, default=20, help="Number of Fibonacci values to plot")
    parser.add_argument("--no-plot", action="store_true", help="Skip plotting the Fibonacci sequence")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    df = load_dataset(args.csv)
    summarize_dataset(df)

    if not args.no_plot:
        fib_sequence = fibonacci_sequence(args.fib)
        plot_fibonacci(fib_sequence)


if __name__ == "__main__":
    main()
