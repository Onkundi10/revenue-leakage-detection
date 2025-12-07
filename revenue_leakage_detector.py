"""
revenue_leakage_detector.py
---------------------------

This script provides a simple framework for detecting revenue leakage in
subscription‑based businesses.  It loads a dataset of customers with
subscription tenure, monthly charges and total charges paid, computes
expected revenue (tenure multiplied by monthly charges) and compares it to
actual revenue received.  Any shortfall is treated as revenue leakage.

Usage:

    python revenue_leakage_detector.py

The script reads data from ``data/synthetic_revenue.csv`` by default, prints
summary statistics to the console and saves a histogram of revenue leakage
to ``output/revenue_leakage_hist.png``.

The sample dataset used in this project is synthetically generated for
demonstration purposes.  In practice you could replace it with real
subscription data, such as the Telco Customer Churn dataset, which
contains monthly and total charges for 7,043 customers【595890463988344†L0-L3】.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt


def load_data(csv_path: str) -> pd.DataFrame:
    """Load the subscription dataset from a CSV file.

    The dataset must include the columns ``tenure``, ``MonthlyCharges`` and
    ``TotalCharges``.  Any non‑numeric values in the ``TotalCharges`` column
    will be coerced to ``NaN``.

    Args:
        csv_path: Path to the CSV file.

    Returns:
        A pandas DataFrame containing the loaded data with an additional
        ``ExpectedRevenue`` and ``RevenueLeakage`` column.
    """
    df = pd.read_csv(csv_path)
    # Ensure numeric columns are numeric
    df['MonthlyCharges'] = pd.to_numeric(df['MonthlyCharges'], errors='coerce')
    df['tenure'] = pd.to_numeric(df['tenure'], errors='coerce')
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    # Compute expected revenue and leakage
    df['ExpectedRevenue'] = df['tenure'] * df['MonthlyCharges']
    df['RevenueLeakage'] = df['ExpectedRevenue'] - df['TotalCharges']
    return df


def compute_statistics(df: pd.DataFrame) -> dict:
    """Compute summary statistics on revenue leakage.

    Args:
        df: DataFrame with a ``RevenueLeakage`` column.

    Returns:
        Dictionary containing total records, total leakage, average leakage
        and the number of customers with positive leakage.
    """
    leakage = df['RevenueLeakage'].dropna()
    stats = {
        'total_records': len(df),
        'total_leakage': leakage.sum(),
        'average_leakage': leakage.mean(),
        'positive_leakage_count': (leakage > 0).sum(),
    }
    return stats


def plot_leakage_histogram(df: pd.DataFrame, output_path: str) -> None:
    """Plot a histogram of the revenue leakage distribution and save it.

    Args:
        df: DataFrame containing a ``RevenueLeakage`` column.
        output_path: File path where the PNG image will be saved.
    """
    leakage = df['RevenueLeakage'].dropna()
    plt.figure()
    plt.hist(leakage, bins=15)
    plt.title('Revenue Leakage Distribution')
    plt.xlabel('Revenue Leakage (USD)')
    plt.ylabel('Number of Customers')
    plt.tight_layout()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)
    plt.close()


def main() -> None:
    """Entry point of the script."""
    # Define paths relative to this script's directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, 'data', 'synthetic_revenue.csv')
    output_path = os.path.join(current_dir, 'output', 'revenue_leakage_hist.png')

    df = load_data(data_path)
    stats = compute_statistics(df)
    # Print summary statistics
    print('Revenue Leakage Summary:')
    print(f"Total customers: {stats['total_records']}")
    print(f"Total leakage: {stats['total_leakage']:.2f}")
    print(f"Average leakage per customer: {stats['average_leakage']:.2f}")
    print(f"Customers with positive leakage: {stats['positive_leakage_count']}")

    # Generate histogram
    plot_leakage_histogram(df, output_path)
    print(f"Histogram saved to {output_path}")


if __name__ == '__main__':
    main()
