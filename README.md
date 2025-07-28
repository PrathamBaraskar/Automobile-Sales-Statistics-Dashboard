# Automobile-Sales-Statistics-Dashboard

This interactive dashboard application, built using Dash, Plotly, and Pandas, provides a visual exploration of historical automobile sales data across different years and economic conditions. Users can toggle between Yearly Statistics and Recession Period Statistics to view key insights on vehicle sales trends, advertising expenditures, and economic factors like unemployment.

📊 Features:
Interactive dropdown filters for report type and year selection

Visualizations using Plotly Express:

Line charts for yearly/monthly sales trends

Bar charts for average vehicle sales by type

Pie charts for advertising expenditure distribution

Multivariate bar charts showing the impact of unemployment

Clean and modular callback structure in Dash

Dynamically enabled/disabled year filter based on the report type

📁 Dataset:
Source: historical_automobile_sales.csv

Contains fields like Year, Month, Automobile_Sales, Vehicle_Type, Advertising_Expenditure, and Unemployment_Rate

⚙️ Technologies Used:
Python

Dash (by Plotly)

Plotly Express

Pandas

🚀 How to Run:
Clone this repository

Install dependencies: pip install dash pandas plotly

Ensure the dataset path is correctly set

Run: python app.py

Open in your browser: http://127.0.0.1:8050/

