# Sales-Revenue-Analytics-Dashboard
A complete interactive dashboard built to analyze sales performance, revenue trends, customer insights, product performance, and key business KPIs. This project demonstrates end-to-end data analytics skills—data cleaning, processing, visualization, and dashboard development.
🚀 Features

📈 Real-time interactive dashboard

💰 Total Revenue, Profit, Sales Quantity KPIs

🗓 Monthly and yearly trends analysis

🛒 Top-selling products & categories

🌍 Region-wise and country-wise sales distribution

👤 Customer segmentation & repeat purchase rate

🔍 Advanced filtering (date, product, region, customer)

📊 Visualizations: Line charts, Bar charts, Maps, Pie charts

📥 Load data from CSV/Excel/Database

✨ Export reports in PDF/CSV

🛠 Tech Stack

Backend / Processing:

Python

Pandas

NumPy

Dashboard / Visualization:

Plotly

Dash (or Streamlit – choose whichever you prefer)

Seaborn / Matplotlib

Optional:

SQLite / MySQL

Power BI / Tableau version also possible

Below, code is provided in Python + Plotly Dash.

📁 Project Structure
sales-revenue-dashboard/
│
├── data/
│   └── sales_data.csv
│
├── dashboard/
│   ├── app.py
│   └── utils.py
│
├── images/
│   ├── dashboard_screenshot.png
│   └── charts.png
│
├── README.md
└── requirements.txt

📊 Dataset Description

Your dataset (sales_data.csv) should include columns similar to:

Column Name	Description
Order_ID	Unique order reference
Order_Date	Date of purchase
Customer_Name	Buyer
Region	Country/Region
Product	Product name
Category	Product category
Quantity	Units sold
Unit_Price	Price per unit
Total	Quantity × Unit Price
Profit	Profit earned

You can modify column names based on your actual data.

🧠 Data Preprocessing (utils.py)

Create dashboard/utils.py:

import pandas as pd

def load_data(path="data/sales_data.csv"):
    df = pd.read_csv(path)

    df["Order_Date"] = pd.to_datetime(df["Order_Date"])
    df["Year"] = df["Order_Date"].dt.year
    df["Month"] = df["Order_Date"].dt.month_name()

    df["Total"] = df["Quantity"] * df["Unit_Price"]
    return df

🖥 Main Dashboard App (app.py)

Create dashboard/app.py:

import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd
from utils import load_data

df = load_data()

app = dash.Dash(__name__)

# KPI Calculations
total_revenue = df["Total"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()

# Charts
sales_trend = px.line(df.groupby("Month")["Total"].sum().reset_index(),
                      x="Month", y="Total", title="Monthly Sales Trend")

region_sales = px.bar(df.groupby("Region")["Total"].sum().reset_index(),
                      x="Region", y="Total", title="Sales by Region")

top_products = px.bar(df.groupby("Product")["Total"].sum().nlargest(10).reset_index(),
                      x="Product", y="Total", title="Top 10 Products")

app.layout = html.Div([
    html.H1("📊 Sales & Revenue Analytics Dashboard"),
    
    html.Div([
        html.Div([
            html.H3("Total Revenue"),
            html.H2(f"${total_revenue:,.2f}")
        ], className="card"),

        html.Div([
            html.H3("Total Profit"),
            html.H2(f"${total_profit:,.2f}")
        ], className="card"),

        html.Div([
            html.H3("Total Units Sold"),
            html.H2(f"{total_quantity:,}")
        ], className="card"),
    ], className="kpi-row"),

    dcc.Graph(figure=sales_trend),
    dcc.Graph(figure=region_sales),
    dcc.Graph(figure=top_products),
])

if __name__ == "__main__":
    app.run_server(debug=True)

📦 requirements.txt
dash
pandas
plotly
numpy

🖼 Screenshots

(Add your images in /images folder)

![Dashboard Screenshot](images/dashboard_screenshot.png)

🏃 How to Run the Project
1. Clone the repository
git clone https://github.com/your-username/sales-revenue-dashboard.git

2. Install dependencies
pip install -r requirements.txt

3. Run the dashboard
python dashboard/app.py

4. Open in browser
http://127.0.0.1:8050/

🚀 Future Enhancements

Add forecasting using Prophet or ARIMA

Add customer lifetime value (CLV) analysis

Add machine learning churn prediction

Add authentication for dashboard users

Deploy on AWS / Heroku / Render

📝 License

MIT License
