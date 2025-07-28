import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

# Load your dataset (update path if needed)
data = pd.read_csv(r"C:\Users\Pratham\Downloads\archive\historical_automobile_sales.csv")

# Preparation for year dropdown
year_list = sorted(data['Year'].unique())

# App creation
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1(
        "Automobile Sales Statistics Dashboard",
        style={'textAlign': 'center', 'color': '#503D36', 'font-size': 24}
    ),
    html.Div([
        html.Label("Select Report-type", style={'font-size': 20, 'color': '#503D36', 'margin-bottom': '10px'}),
        dcc.Dropdown(
            id='dropdown-statistics',
            options=[
                {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
                {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
            ],
            placeholder='Select a report type',
            value=None,
            style={
                'width': '80%',
                'padding': '3px',
                'font-size': '20px',
                'text-align-last': 'center',
                'margin': 'auto'
            }
        ),
    ], style={'padding': '10px', 'margin-bottom': '20px', 'textAlign': 'center'}),
    html.Div([
        html.Label("Select Year", style={'font-size': 20, 'color': '#503D36', 'margin-bottom': '10px'}),
        dcc.Dropdown(
            id='select-year',
            options=[{'label': i, 'value': i} for i in year_list],
            placeholder='Select-year',
            value=None,
            style={
                'width': '80%',
                'padding': '3px',
                'font-size': '20px',
                'text-align-last': 'center',
                'margin': 'auto'
            }
        )
    ], style={'padding': '10px', 'margin-bottom': '20px', 'textAlign': 'center'}),
    html.Div([
        html.Div(id='output-container', className='chart-grid', style={'display': 'flex', 'flexDirection': 'column'})
    ])
])


@app.callback(
    Output('select-year', 'disabled'),
    Input('dropdown-statistics', 'value')
)
def update_input_container(statistics_selected):
    if statistics_selected == 'Yearly Statistics':
        return False
    else:
        return True


@app.callback(
    Output('output-container', 'children'),
    [Input('dropdown-statistics', 'value'),
     Input('select-year', 'value')]
)
def update_output_container(selected_statistics, input_year):
    if selected_statistics == 'Recession Period Statistics':
        # Filter for recession periods
        recession_data = data[data['Recession'] == 1]

        # 1. Average Automobile Sales Fluctuation Over Recession
        yearly_rec = recession_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        R_chart1 = dcc.Graph(
            figure=px.line(yearly_rec, x='Year', y='Automobile_Sales',
                           title="Automobile Sales Fluctuate Over Recession Period (Year-wise)")
        )

        # 2. Average Number of Vehicles Sold by Vehicle Type
        average_sales = recession_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        R_chart2 = dcc.Graph(
            figure=px.bar(average_sales, x='Vehicle_Type', y='Automobile_Sales',
                          title="Average Vehicles Sold by Vehicle Type (Recession)")
        )

        # 3. Pie chart for total expenditure share by vehicle type during recessions
        exp_rec = recession_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        R_chart3 = dcc.Graph(
            figure=px.pie(exp_rec, values='Advertising_Expenditure', names='Vehicle_Type',
                          title="Total Expenditure Share by Vehicle Type (Recession)")
        )

        # 4. Bar chart for effect of unemployment rate
        unemp_data = recession_data.groupby(['unemployment_rate', 'Vehicle_Type'])['Automobile_Sales'].mean().reset_index()
        R_chart4 = dcc.Graph(
            figure=px.bar(unemp_data, x='Vehicle_Type', y='Automobile_Sales', color='unemployment_rate',
                          labels={'unemployment_rate': 'Unemployment Rate', 'Automobile_Sales': 'Avg Automobile Sales'},
                          title='Effect of Unemployment Rate on Vehicle Type and Sales (Recession)')
        )

        return [
            html.Div(className='chart-item', children=[html.Div(children=R_chart1), html.Div(children=R_chart2)],
                     style={'display': 'flex'}),
            html.Div(className='chart-item', children=[html.Div(children=R_chart3), html.Div(children=R_chart4)],
                     style={'display': 'flex'})
        ]

    elif input_year and selected_statistics == 'Yearly Statistics':
        yearly_data = data[data['Year'] == input_year]

        # 1. Yearly Automobile Sales using Line chart for the whole period
        yas = data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        Y_chart1 = dcc.Graph(
            figure=px.line(yas, x='Year', y='Automobile_Sales',
                           title='Yearly Automobile Sales (All Years)')
        )

        # 2. Total Monthly Automobile Sales Using Line Chart
        mas = yearly_data.groupby('Month')['Automobile_Sales'].sum().reset_index()
        Y_chart2 = dcc.Graph(
            figure=px.line(mas, x='Month', y='Automobile_Sales',
                           title='Total Monthly Automobile Sales ({})'.format(input_year))
        )

        # 3. Average Vehicles Sold by Type in the Selected Year (Bar Chart)
        avr_vdata = yearly_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        Y_chart3 = dcc.Graph(
            figure=px.bar(avr_vdata, x='Vehicle_Type', y='Automobile_Sales',
                          title='Average Vehicles Sold by Type ({})'.format(input_year))
        )

        # 4. Total Advertisement Expenditure for Each Vehicle (Pie)
        exp_data = yearly_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        Y_chart4 = dcc.Graph(
            figure=px.pie(exp_data, values='Advertising_Expenditure', names='Vehicle_Type',
                          title='Total Advertisement Expenditure by Vehicle Type ({})'.format(input_year))
        )

        return [
            html.Div(className='chart-item', children=[html.Div(children=Y_chart1), html.Div(children=Y_chart2)],
                     style={'display': 'flex'}),
            html.Div(className='chart-item', children=[html.Div(children=Y_chart3), html.Div(children=Y_chart4)],
                     style={'display': 'flex'})
        ]
    else:
        return []

if __name__ == '__main__':
    app.run(debug=True)
