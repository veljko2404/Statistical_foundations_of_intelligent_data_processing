import pandas as pd
import numpy as np
import scipy.stats as stats
import math

data = pd.read_csv("Bank_Churn.csv")

geography = np.asarray(data["Geography"])
estimated_salary = np.asarray(data["EstimatedSalary"])

estimated_salary_france = estimated_salary[geography == "France"]
print(estimated_salary_france.mean())
print(estimated_salary.mean())

t_stat, p_value = stats.ttest_1samp(a=estimated_salary_france, popmean=estimated_salary.mean())
print(f"T-statistic: {t_stat:.2f}, P-value: {p_value:.4f}")

print(stats.t.ppf(q=0.025,df=estimated_salary_france.size-1))
print(stats.t.ppf(q=0.975,df=estimated_salary_france.size-1))
sigma = estimated_salary_france.std()/math.sqrt(estimated_salary_france.size)

print(stats.t.interval(0.95,
                       df = estimated_salary_france.size-1,
                       loc = estimated_salary_france.mean(),
                       scale= sigma))
