import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load employee performance data
data = pd.read_csv("employee_data.csv")

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("HR Analytics Dashboard"),
    dcc.Graph(
        figure=px.bar(data, x="employee_name", y="performance_score", color="department", title="Employee Performance")
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)
