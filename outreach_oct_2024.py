# =================================== IMPORTS ================================= #

import pandas as pd 
import plotly.express as px
import os
import plotly.graph_objects as go
import dash
from dash import dcc, html
# print('System Version:', sys.version)

# -------------------------------------- DATA ------------------------------------------- #

current_dir = os.getcwd()
script_dir = os.path.dirname(os.path.abspath(__file__))
data_path1 = 'data/BMHC_Navigation_Outreach_Impact_Report.xlsx'
file_path1 = os.path.join(script_dir, data_path1)

# Read data from excel file
data = pd.read_excel(file_path1)

# df_r = data_r2.copy()
df = data.copy()

# Concatenate dataframes
# df = pd.concat([data1, data2], ignore_index=True)

# Trim leading and trailing whitespaces from column names
# df_r.columns = df_r.columns.str.strip()
df.columns = df.columns.str.strip()

# Define a discrete color sequence
color_sequence = px.colors.qualitative.Plotly

# print(df_m.head())
# print('Total entries: ', len(df))
# print('Column Names: \n', df.columns)
# print('DF Shape:', df.shape)
# print('Dtypes: \n', df.dtypes)
# print('Info:', df.info())
# print("Amount of duplicate rows:", df.duplicated().sum())

# print('Current Directory:', current_dir)
# print('Script Directory:', script_dir)
# print('Path to data:',file_path)

# ================================= Columns ================================= #

# Column Names: 
#  Index([
#        'Timestamp', 
#        'Which outreach event are you reporting on?', 
#        'Date:',
#        'Event Name', 
#        'Partner Name:', 
#        'Discussion Purpose', 
#        'Defined Outcome',
#        'Number of Appointments Scheduled:', 
#        'Primary Care Type:',
#        'SDoH Service Type', 
#        'Number of MAP applications',
#        'Number of SDoH services coordinated',
#        'Number of health checks rendered'],
#       dtype='object')

# ------------------------------- Missing Values ----------------------------------- #

# missing = df.isnull().sum()
# print('Columns with missing values before fillna: \n', missing[missing > 0])


# ============================== Data Preprocessing ========================== #



# -----------------------------------------------------------------------------

# Get the distinct values in column

# distinct_service = df['What service did/did not complete?'].unique()
# print('Distinct:\n', distinct_service)

# ------------------------------------ SQL ---------------------------------------

# Connect to SQL
# con = sqlite3.connect("bmhc_2024.db")
# cur = con.cursor()

# df.to_sql("bmhc_outreach_oct_2024", con, if_exists='replace', index=False, method="multi")

# # # Show list of all tables in db.
# # # tables = pd.read_sql_query("""
# # #   SELECT name 
# # #   FROM sqlite_master 
# # #   WHERE type = 'table';
# # # """, con)
# # # print("Tables in the database:\n", tables)

# # # # Check if data is inserted correctly
# # # df_check = pd.read_sql_query("SELECT * FROM bmhc_responses_q3_2024 LIMIT 5;", con)
# # # print(df_check)

# con.close()

# ========================= Filtered DataFrames ========================== #

# Datafram where column 'Which outreach event are you reporting on?' is equal to 'Care Coordination Scheduling'
df_care = df[df['Which outreach event are you reporting on?'] == 'Care Coordination Scheduling']

# Include all columns except 'Timestamp'
care_columns = [
    'Which outreach event are you reporting on?',
    'Date:',
    'Event Name', 
    'Partner Name:', 
    'Discussion Purpose', 
    'Defined Outcome',
    'Number of Appointments Scheduled:',
    'Primary Care Type:',
    'SDoH Service Type',
    'Number of MAP applications',
    'Number of SDoH services coordinated',
    'Number of health checks rendered'
]

df_care_filtered = df_care[care_columns]

# Datafram where column 'Which outreach event are you reporting on?' is equal to 'Community Outreach Event'
df_community = df[df['Which outreach event are you reporting on?'] == 'Community Outreach Event']

# List of columns to include
community_columns = [
    'Which outreach event are you reporting on?', 
    'Date:',
    'Event Name', 
    'Partner Name:', 
    'Discussion Purpose', 
    'Defined Outcome',
    'Number of health checks rendered'
]

# Create a new DataFrame with only the specified columns
df_community_filtered = df_community[community_columns]

# Datafram where column 'Which outreach event are you reporting on?' is equal to 'Partnership Engagement Meeting'
df_partnership = df[df['Which outreach event are you reporting on?'] == 'Partnership Engagement Meeting']

partnership_columns = [
    'Which outreach event are you reporting on?', 
    'Date:',
    'Event Name', 
    'Partner Name:', 
    'Discussion Purpose', 
    'Defined Outcome'
]

df_partnership_filtered = df_partnership[partnership_columns]

# # # ========================== DataFrame Tables ========================== #

# Care Coordination Scheduling Table
care_coordination_table = go.Figure(data=[go.Table(
    # columnwidth=[50, 50, 50],  # Adjust the width of the columns
    header=dict(
        values=list(df_care_filtered.columns),
        fill_color='paleturquoise',
        align='center',
        height=30,  # Adjust the height of the header cells
        # line=dict(color='black', width=1),  # Add border to header cells
        font=dict(size=12)  # Adjust font size
    ),
    cells=dict(
        values=[df_care_filtered[col] for col in df_care_filtered.columns],
        fill_color='lavender',
        align='left',
        height=25,  # Adjust the height of the cells
        # line=dict(color='black', width=1),  # Add border to cells
        font=dict(size=12)  # Adjust font size
    )
)])

# Community Outreach Table
community_table = go.Figure(data=[go.Table(
    # columnwidth=[50, 50, 50],  # Adjust the width of the columns
    header=dict(
        values=list(df_community_filtered.columns),
        fill_color='paleturquoise',
        align='center',
        height=30,  # Adjust the height of the header cells
        # line=dict(color='black', width=1),  # Add border to header cells
        font=dict(size=12)  # Adjust font size
    ),
    cells=dict(
        values=[df_community_filtered[col] for col in df_community_filtered.columns],
        fill_color='lavender',
        align='left',
        height=25,  # Adjust the height of the cells
        # line=dict(color='black', width=1),  # Add border to cells
        font=dict(size=12)  # Adjust font size
    )
)])

# Partnership Engagement Table
partnership_table = go.Figure(data=[go.Table(
    # columnwidth=[50, 50, 50],  # Adjust the width of the columns
    header=dict(
        values=list(df_partnership_filtered.columns),
        fill_color='paleturquoise',
        align='center',
        height=30,  # Adjust the height of the header cells
        # line=dict(color='black', width=1),  # Add border to header cells
        font=dict(size=12)  # Adjust font size
    ),
    cells=dict(
        values=[df_partnership_filtered[col] for col in df_partnership_filtered.columns],
        fill_color='lavender',
        align='left',
        height=25,  # Adjust the height of the cells
        # line=dict(color='black', width=1),  # Add border to cells
        font=dict(size=12)  # Adjust font size
    )
)])

# ============================== Dash Application ========================== #

app = dash.Dash(__name__)
server= app.server

app.layout = html.Div(children=[ 

    html.Div(className='divv', children=[ 
        
        html.H1('BMHC Outreach Report October 2024', 
        className='title'),

        html.A(
        'Repo',
        href='https://github.com/CxLos/Outreach_Oct_2024',
        className='btn')
    ]),    

# Data Table Care Coordination
html.Div(
    className='row0',
    children=[

        html.Div(
            className='table',
            children=[
                html.H1(
                    className='table-title1',
                    children='Care Coordination'
                )
            ]
        ),
        html.Div(
            className='highlights',
            children=[
                html.Div(
                    className='highs-activity',
                    children=[
                        html.H1(
                            className='high1',
                            children=['Appointments Scheduled:']
                        ),
                        html.H1(
                            className='high2',
                            children=['10']
                        ),
                    ],
                ),
                html.Div(
                    className='highs-public',
                    children=[
                        html.H1(
                            className='high1',
                            children=['MAP Applications:']
                        ),
                        html.H1(
                            className='high2',
                            children=['17']
                        ),
                    ],
                ),
                html.Div(
                    className='highs-product',
                    children=[
                        html.H1(
                            className='high1',
                            children=['SDoH Services Coordinated:']
                        ),
                        html.H1(
                            className='high2',
                            children=['20']
                        ),
                    ],
                ),
                html.Div(
                    className='highs',
                    children=[
                        html.H1(
                            className='high1',
                            children=['Health Checks Rendered:']
                        ),
                        html.H1(
                            className='high2',
                            children=['62']
                        ),
                    ],
                ),

            ]
        ),
        html.Div(
            className='table2', 
            children=[
                dcc.Graph(
                    className='data',
                    figure=care_coordination_table
                )
            ]
        )
    ]
),

# Data Community Outreach
html.Div(
    className='row0',
    children=[
        html.Div(
            className='table',
            children=[
                html.H1(
                    className='table-title',
                    children='Community Outreach'
                )
            ]
        ),
                html.Div(
            className='highlights',
            children=[
                html.Div(
                    className='highs-activity',
                    children=[
                        html.H1(
                            className='high1',
                            children=['Activities:']
                        ),
                        html.H1(
                            className='high2',
                            children=['2']
                        ),
                    ],
                ),
                html.Div(
                    className='highs-public',
                    children=[
                        html.H1(
                            className='high1',
                            children=['Health Checks Rendered:']
                        ),
                        html.H1(
                            className='high2',
                            children=['48']
                        ),
                    ],
                ),
            ]
        ),
        html.Div(
            className='table2', 
            children=[
                dcc.Graph(
                    className='data',
                    figure=community_table
                )
            ]
        )
    ]
),

# Data Table Partnership Engagement
html.Div(
    className='row0',
    children=[
        html.Div(
            className='table',
            children=[
                html.H1(
                    className='table-title',
                    children='Partnership Engagement'
                )
            ]
        ),
                html.Div(
            className='highlights',
            children=[
                html.Div(
                    className='highs-activity',
                    children=[
                        html.H1(
                            className='high1',
                            children=['Activities:']
                        ),
                        html.H1(
                            className='high2',
                            children=['2']
                        ),
                    ],
                ),
            ]
        ),
        html.Div(
            className='table2', 
            children=[
                dcc.Graph(
                    className='data',
                    figure=partnership_table
                )
            ]
        )
    ]
),
])

# Callback function
# @app.callback(
#     Output('', 'figure'),
#     [Input('', 'value')]
# )

if __name__ == '__main__':
    app.run_server(debug=
                   True)
                #    False)
# ----------------------------------------------- Updated Database ----------------------------------------

# updated_path = 'data/bmhc_q4_2024_cleaned.xlsx'
# data_path = os.path.join(script_dir, updated_path)
# df.to_excel(data_path, index=False)
# print(f"DataFrame saved to {data_path}")

# updated_path1 = 'data/service_tracker_q4_2024_cleaned.csv'
# data_path1 = os.path.join(script_dir, updated_path1)
# df.to_csv(data_path1, index=False)
# print(f"DataFrame saved to {data_path1}")

# -------------------------------------------- KILL PORT ---------------------------------------------------

# netstat -ano | findstr :8050
# taskkill /PID 24772 /F
# npx kill-port 8050

# ---------------------------------------------- Host Application -------------------------------------------

# 1. pip freeze > requirements.txt
# 2. add this to procfile: 'web: gunicorn outreach_oct_2024:server'
# 3. heroku login
# 4. heroku create
# 5. git push heroku main

# Create venv 
# virtualenv venv 
# source venv/bin/activate # uses the virtualenv

# Update PIP Setup Tools:
# pip install --upgrade pip setuptools

# Install all dependencies in the requirements file:
# pip install -r requirements.txt

# Check dependency tree:
# pipdeptree
# pip show package-name

# Remove
# pypiwin32
# pywin32
# jupytercore

# ----------------------------------------------------

# Name must start with a letter, end with a letter or digit and can only contain lowercase letters, digits, and dashes.

# Heroku Setup:
# heroku login
# heroku create outreach-oct-2024
# heroku git:remote -a outreach-oct-2024
# git push heroku main

# Clear Heroku Cache:
# heroku plugins:install heroku-repo
# heroku repo:purge_cache -a outreach-oct-2024

# Set buildpack for heroku
# heroku buildpacks:set heroku/python

# rm -rf ~$bmhc_data_2024_cleaned.xlsx
# rm -rf ~$bmhc_data_2024.xlsx
# rm -rf ~$bmhc_q4_2024_cleaned2.xlsx