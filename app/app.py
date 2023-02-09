# Import necessary libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

# Connect to the database
df = pd.read_sql('SELECT * FROM auto', conn)

# Create a Dash app
app = dash.Dash()

# Create a dropdown component to select columns
column_options = [{'label': i, 'value': i} for i in df.columns if df[i].dtype in ['int64', 'float64']]
column_selector = dcc.Dropdown(id='column-selector', options=column_options, value=df.columns[0])

# Create a scatter plot using the selected columns
scatter_plot = dcc.Graph(id='scatter-plot')

# Define the layout of the app
app.layout = html.Div([
    html.H1('Auto Database Scatter Plot'),
    html.Div([
        html.Label('Select X-axis Column'),
        column_selector,
    ]),
    html.Div([
        html.Label('Select Y-axis Column'),
        column_selector,
    ]),
    scatter_plot
])

# Define a callback to update the scatter plot
@app.callback(
    dash.dependencies.Output('scatter-plot', 'figure'),
    [dash.dependencies.Input('column-selector', 'value')])
def update_scatter_plot(columns):
    x_column = columns[0]
    y_column = columns[1]
    return {
        'data': [{
            'x': df[x_column],
            'y': df[y_column],
            'type': 'scatter'
        }],
        'layout': {
            'title': f'{x_column} vs {y_column}'
        }
    }

# Run the app
if name == 'main':
    app.run_server()
