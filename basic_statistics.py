import pandas as pd
import numpy as np
from statistics import mode

data = pd.read_csv("Bank_Churn.csv")

credit_score = np.asarray(data["CreditScore"])  # Customer's credit score
geography = np.asarray(data["Geography"])  # The country where the customer resides
gender = np.asarray(data["Gender"])  # The customer's gender (Male or Female)
age = np.asarray(data["Age"])  # The customer's age
tenure = np.asarray(data["Tenure"])  # The number of years the customer has been with the bank
balance = np.asarray(data["Balance"])  # The customer's account balance
has_credit_card = np.asarray(data["HasCrCard"])  # Whether the customer has a credit card (1 = yes, 0 = no)
estimated_salary = np.asarray(data["EstimatedSalary"])  # The estimated salary of the customer

all_data = {
    "Credit Score": credit_score,
    "Age": age,
    "Tenure": tenure,
    "Balance": balance,
    "Estimated Salary": estimated_salary,
}

for key, value in all_data.items():
    print(f"{key}")
    print(f"Mean: {value.mean():.2f}")
    print(f"Median: {np.median(value):.2f}")
    print(f"Mode: {mode(value):.2f}")
    print(f"Min: {value.min():.2f}")
    print(f"Max: {value.max():.2f}")
    print(f"25th percentile: {np.quantile(value, 0.25):.2f}")
    print(f"75th percentile: {np.quantile(value, 0.75):.2f}")
    print(f"Standard Deviation: {value.std():.2f}\n")
