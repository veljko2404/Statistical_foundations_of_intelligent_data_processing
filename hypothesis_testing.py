import pandas as pd
import numpy as np
import scipy.stats as stats
import math

data = pd.read_csv("Bank_Churn.csv")

geography = np.asarray(data["Geography"])
gender = np.asarray(data["Gender"])
balance = np.asarray(data["Balance"])
estimated_salary = np.asarray(data["EstimatedSalary"])

# One-Sample T-Test
# We will check if estimated salary is significantly different in each
# of the 3 countries from data (France, Germany and Spain)

estimated_salary_france = estimated_salary[geography == "France"]
estimated_salary_spain = estimated_salary[geography == "Spain"]
estimated_salary_germany = estimated_salary[geography == "Germany"]

salaries = {
    "France": estimated_salary_france,
    "Spain": estimated_salary_spain,
    "Germany": estimated_salary_germany
}

print(f"Overall mean estimated salary: {estimated_salary.mean():.2f}\n")

for country, salary in salaries.items():
    print(f"Mean estimated salary in {country}: {salary.mean():.2f}")
    t_stat, p_value = stats.ttest_1samp(a=salary, popmean=estimated_salary.mean())
    print(f"T-statistic: {t_stat:.2f}, P-value: {p_value:.4f}")

    if p_value > 0.05:
        print(f"The mean salary in {country} is significantly different")
    else:
        print(f"No significant difference in {country}")

    sigma = salary.std(ddof=1) / math.sqrt(salary.size)
    conf_int = stats.t.interval(0.95, df=salary.size - 1, loc=salary.mean(), scale=sigma)
    print(f"95% Confidence Interval: [{conf_int[0]:.2f}, {conf_int[1]:.2f}]\n")


# Two-Sample T-Test
# Here we will check whether means of France and Spain differ

print(stats.ttest_ind(a=estimated_salary_france, b=estimated_salary_spain, equal_var=False))

