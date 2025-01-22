import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Bank_Churn.csv")

credit_score = df["CreditScore"]
geography = df["Geography"]
gender = df["Gender"]
age = df["Age"]
tenure = df["Tenure"]
balance = df["Balance"]
has_credit_card = df["HasCrCard"]
estimated_salary = df["EstimatedSalary"]

data = pd.DataFrame({
    "Credit score": credit_score,
    "Age": age,
    "Tenure": tenure,
    "Balance": balance,
    "Estimated Salary": estimated_salary
})

corr_matrix = data.corr()

sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")

plt.show()
