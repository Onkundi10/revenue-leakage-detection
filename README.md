# Revenue Leakage Detection

This project demonstrates a simple workflow for detecting **revenue leakage** in
subscription‑based businesses.  It uses a synthetic dataset inspired by the
Telco Customer Churn dataset.  The original Telco dataset contains 7,043
customers and includes fields such as customerID, tenure, MonthlyCharges and
TotalCharges【595890463988344†L0-L3】.  Each record represents a customer’s subscription
history with a fictional telecommunications company【595890463988344†L0-L3】.  In our synthetic
dataset we retain the key numerical fields—tenure, MonthlyCharges and
TotalCharges—to compute expected revenue (tenure × MonthlyCharges) and
compare it with actual charges.

## Project features

* **Data loading:** Read a CSV file of customer subscription data into a
  pandas DataFrame.
* **Revenue computation:** Calculate expected revenue and revenue leakage for
  each customer by comparing the expected revenue to the total charges paid.
* **Statistics:** Compute summary statistics including total leakage, average
  leakage and the number of customers with positive leakage.
* **Visualization:** Generate a histogram of the revenue leakage distribution
  and save it to an image file.

## Getting started

1. **Clone the repository** (or download the ZIP) and change into its directory.
2. **Install the required dependencies.**  The script depends on
   `pandas` and `matplotlib`:

   ```bash
   pip install pandas matplotlib
   ```

3. **Run the analysis script:**

   ```bash
   python revenue_leakage_detector.py
   ```

   The script will print a summary of revenue leakage to the console and
   generate a histogram saved to `output/revenue_leakage_hist.png`.

## Files and directories

| Path | Description |
| --- | --- |
| `data/synthetic_revenue.csv` | Synthetic dataset with customer tenure, monthly charges and total charges used for analysis. |
| `revenue_leakage_detector.py` | Python script that loads the data, computes revenue leakage, prints statistics and generates a histogram. |
| `output/revenue_leakage_hist.png` | Output histogram showing the distribution of revenue leakage among customers. |
| `README.md` | Project documentation and usage instructions. |

## License

This project is released under the MIT License.  The synthetic dataset is
derived from publicly available fields in the Telco Customer Churn data
source【595890463988344†L0-L3】.
