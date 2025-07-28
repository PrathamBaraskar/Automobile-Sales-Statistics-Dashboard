# Automobile-Sales-Statistics-Dashboard

An interactive dashboard built with Dash, Plotly, and Pandas to analyze historical automobile sales data. The app offers two modes—Yearly Statistics and Recession Period Statistics—with a variety of insightful visualizations related to vehicle sales, advertisement spending, and economic indicators.

📊 Dashboard Features
🔄 Toggle between two report types:

Yearly Statistics: Select a specific year to analyze monthly trends, vehicle types, and ad expenditure.

Recession Period Statistics: View trends during recession years, including unemployment effects and ad spend breakdown.

📈 Dynamic visualizations:

Line charts for sales trends over time

Bar charts for average sales by vehicle type

Pie charts showing advertising expenditure distribution

Multivariate charts correlating unemployment rate and vehicle sales

🎯 User interactivity:

Dropdown controls to filter by report type and year

Conditional enabling/disabling of filters based on selection

📁 Dataset Overview
File: historical_automobile_sales.csv

Key Columns:

Year, Month

Automobile_Sales

Vehicle_Type

Advertising_Expenditure

unemployment_rate

Recession (1 if recession, else 0)

🛠️ Tech Stack
Frontend/Interactivity: Dash by Plotly

Visualization: Plotly Express

Data Manipulation: Pandas

Language: Python 3.x

🚀 Getting Started
🔧 Requirements
bash
Copy
Edit
pip install dash pandas plotly
▶️ Running the App
Clone this repository:

bash
Copy
Edit
git clone https://github.com/your-username/automobile-sales-dashboard.git
cd automobile-sales-dashboard
Replace the dataset path in app.py if necessary.

Run the app:

bash
Copy
Edit
python app.py
Open your browser and go to:

cpp
Copy
Edit
http://127.0.0.1:8050/
📷 Screenshots
<img width="1213" height="723" alt="Yearly report graphs" src="https://github.com/user-attachments/assets/f234bf1f-f947-4c77-87e7-5974bd25a5eb" />

💡 Future Improvements
Add time-series forecasting for future sales

Enable CSV upload to test with different datasets

Improve layout responsiveness for mobile

Deploy on Heroku or Render for live demo

📌 License
This project is open-source and available under the MIT License.

🙋‍♂️ Author
Pratham Baraskar
Connect with me on LinkedIn [https://www.linkedin.com/in/prathambaraskar/] | View more projects on GitHub 
