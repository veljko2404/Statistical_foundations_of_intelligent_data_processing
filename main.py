import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("Bank_Churn.csv")

credit_score = np.asarray(data["CreditScore"])  # Customer's credit score
geography = np.asarray(data["Geography"])  # The country where the customer resides
gender = np.asarray(data["Gender"])  # The customer's gender (Male or Female)
age = np.asarray(data["Age"])  # The customer's age
tenure = np.asarray(data["Tenure"])  # The number of years the customer has been with the bank
balance = np.asarray(data["Balance"])  # The customer's account balance
has_credit_card = np.asarray(data["HasCrCard"])  # Whether the customer has a credit card (1 = yes, 0 = no)
estimated_salary = np.asarray(data["EstimatedSalary"])  # The estimated salary of the customer

plt.scatter(age, balance)
plt.show()
plt.scatter(credit_score, age)
plt.show()
plt.scatter(age, tenure)
plt.show()
plt.scatter(age, estimated_salary)
plt.show()
plt.scatter(age, gender)
plt.show()
