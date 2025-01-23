from scipy.stats import kstest
import pandas as pd
from fitter import Fitter
import numpy as np

df = pd.read_csv("Bank_Churn.csv")

balance=np.asarray(df["Balance"])
balance_without_0 = balance[balance!=0] # removing 0 values from balance

all_data = {
    "Credit Score": df["CreditScore"],
    "Age": df["Age"],
    "Tenure": df["Tenure"],
    "Balance": df["Balance"],
    "Balance without 0" : balance_without_0,
    "Estimated Salary": df["EstimatedSalary"],
}

for key, value in all_data.items():
    f = Fitter(value, distributions=['uniform', 'norm', 'expon'])
    f.fit()
    best_distribution = list(f.get_best().keys())[0] # returns the best distribution
    print(f"{key} fits best for {best_distribution} distribution")
    if best_distribution == "uniform":
        statistic, p_value = kstest(value, 'uniform', args=(value.min(), value.max()))
        print("K-S Test Statistic:", statistic)
        print("P-value:", p_value)
    elif best_distribution == "norm":
        statistic, p_value = kstest(value, 'norm', args=(np.mean(value), np.std(value)))
        print("K-S Test Statistic:", statistic)
        print("P-value:", p_value)
    elif best_distribution == "expon":
        statistic, p_value = kstest(value, 'expon', args=(0, np.mean(value)))
        print("K-S Test Statistic:", statistic)
        print("P-value:", p_value)
