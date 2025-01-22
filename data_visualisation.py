import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go

df = pd.read_csv("Bank_Churn.csv")

credit_score = df["CreditScore"]
geography = df["Geography"]
gender = df["Gender"]
age = df["Age"]
tenure = df["Tenure"]
balance = df["Balance"]
has_credit_card = df["HasCrCard"]
estimated_salary = df["EstimatedSalary"]

fig = make_subplots(rows=2, cols=4, subplot_titles=(
"Credit score", "Country", "Gender", "Age", "Tenure", "Balance", "Has a credit card", "Estimated salary"))

fig.add_trace(go.Histogram(x=credit_score), row=1, col=1)
fig.add_trace(go.Histogram(x=geography), row=1, col=2)
fig.add_trace(go.Histogram(x=gender), row=1, col=3)
fig.add_trace(go.Histogram(x=age), row=1, col=4)
fig.add_trace(go.Histogram(x=tenure), row=2, col=1)
fig.add_trace(go.Histogram(x=balance), row=2, col=2)
fig.add_trace(go.Histogram(x=has_credit_card), row=2, col=3)
fig.add_trace(go.Histogram(x=estimated_salary), row=2, col=4)

fig.show()
