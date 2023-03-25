import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def root():
    return """
    <h1>Hello, World!</h1>
    <button onclick="window.location.href='/electronics'">Electronics</button>
    <button onclick="window.location.href='/financial'">Financial</button>
    """


@app.route("/electronics")
def bar_graph():
    # Group data by month and product, and sum the quantity
    grouped_df = bar.groupby(["Month", "Product"])["Quantity"].sum().reset_index()

    # Pivot the data to create a matrix with products as columns and months as rows
    pivoted_df = grouped_df.pivot(index="Month", columns="Product", values="Quantity")

    # Create chart data
    chart_data = {
        "labels": pivoted_df.index.tolist(),
        "datasets": [
            {"label": col, "data": pivoted_df[col].tolist()} for col in pivoted_df.columns
        ]
    }

    return render_template("bar.html", chart_data=chart_data)


@app.route("/financial")
def line_graph():
    # Sort the dataframe by Month Number and Year
    line.sort_values(by=['Year', 'Month Number'], inplace=True)

    # Create a list of all unique months in the dataframe
    months = []
    for year in line['Year'].unique():
        for month_num in line[line['Year'] == year]['Month Number'].unique():
            month = f"{month_num}/{year}"
            months.append(month)

    # Create a dictionary to store the profits for each country
    data = {}
    for country in line['Country'].unique():
        country_data = []
        for month in months:
            month_num, year = map(int, month.split('/'))
            profit = line[(line['Country'] == country) & (line['Month Number'] == month_num) & (line['Year'] == year)]['Profit'].sum()
            country_data.append(profit)
        data[country] = country_data

    # Create the chart data dictionary
    chart_data = {
        'labels': months,
        'datasets': []
    }
    colors = ['red', 'blue', 'green', 'orange', 'purple']
    for i, country in enumerate(line['Country'].unique()):
        dataset = {
            'label': country,
            'data': data[country],
            'backgroundColor': colors[i],
            'borderColor': colors[i]
        }
        chart_data['datasets'].append(dataset)

    return render_template("line.html", chart_data=chart_data)


if __name__ == "__main__":
    # Read data from input file using Pandas
    bar = pd.read_csv("data/electronics.csv")
    line = pd.read_excel("data/financial.xlsx")
    
    app.run()
