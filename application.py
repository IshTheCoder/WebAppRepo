from dash.dependencies import Input, Output
import dash
import dash_core_components as dcc
import dash_html_components as html
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from pca import k_means, top5_img
from scatter import scatter_plot_in
from navbar import Navbar
from pie_chart import draw_pie_chart
import dash_bootstrap_components as dbc
import flask
import matplotlib
from effi import plot_most_effi_figure
from dash_table import DataTable
from sim_com import sim_com
from figure_generate import *


def get_options(list_stocks):
    dict_list = []
    for i in list_stocks:
        dict_list.append({'label': i, 'value': i})

    return dict_list


matplotlib.use('agg')

# for page6
path = "data/data_cleaned/pca_data/2015_pca_table.csv"
df = pd.read_csv(path)
names = df['PLAYER_NAME']
['PLAYER_NAME', 'TEAM_NAME', 'total_poss', 'Similarity Score', 'Complement Score']
nameList = {'PLAYER_NAME': 'Player Name',
            'TEAM_NAME': 'Team Name',
            'total_poss': 'Total Poss',
            'Similarity Score': 'Similarity Score',
            'Complement Score': 'Complement Score'}

app_flask = flask.Flask(__name__)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED], server=app_flask, url_base_pathname='/page1/')

app2 = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED], server=app_flask, url_base_pathname='/page2/')

app3 = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED], server=app_flask, url_base_pathname='/page3/')

app4 = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED], server=app_flask, url_base_pathname='/page4/')

app5 = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED], server=app_flask, url_base_pathname='/page5/')

app6 = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED], server=app_flask, url_base_pathname='/page6/')

nav = Navbar()

app.layout = html.Div(
    children=[
        html.Div([nav]),
        html.Div(className='row',  # Define the row element
                 children=[
                     html.Div(className='four columns div-user-controls',
                              children=[
                                  html.H2('Description'),
                                  html.Div(id='app1text', children='This is a K-means clustering of player roles over the last 5 years, based on play-style. Using the distribution and efficiency of play-style, we have managed to redefine player roles over the period of the analytics shift in basketball. As a team or a fanatic, this allows you to get a better understanding of the NBA landscape and find players that fit the modern roles better.')
                              ]
                              ),  # Define the left element
                     html.Div(className='eight columns div-for-charts bg-grey',
                              children=[
                                  html.H2('K-Means clustering for new-era player roles'),
                                  dcc.Graph(
                                      figure=update_app1(), config={'displayModeBar': True}
                                  )
                              ])  # Define the right element
                 ])
    ])

app2.layout = html.Div(
    children=[
        html.Div([nav]),
        html.Div(className='row',  # Define the row element
                 children=[
                     html.Div(className='four columns div-user-controls',
                              children=[
                                  html.H2('Description'),
                                  html.Div(id='app2text', children='This plot allows us to see how player volume scales with scoring efficiency. This is an important plot, as in order to understand extraordinary scoring, we must also understand scoring burdens. As a team, this will allow you to contextualize your players performances against the rest of the league. As a fanatic you can just enjoy the greatness of the outliers.')
                              ]
                              ),  # Define the left element
                     html.Div(className='eight columns div-for-charts bg-grey',
                              children=[
                                  html.H2('Scoring Efficiency vs Volume'),
                                  dcc.Graph(
                                      figure=update_app2(), config={'displayModeBar': True}
                                  )
                              ])  # Define the right element
                 ])
    ])

app3.layout = html.Div(
    children=[
        html.Div([nav]),
        html.Div(className='row',  # Define the row element
                 children=[
                     html.Div(className='four columns div-user-controls',
                              children=[
                                  html.H2('Years options'),
                                  html.Div(className='div-for-dropdown',
                                           children=[
                                               dcc.Dropdown(id='years',
                                                            options=get_options(
                                                                ['2015', '2016', '2017', '2018', '2019']),
                                                            multi=False,
                                                            value='2015',
                                                            style={'backgroundColor': '#1E1E1E'},
                                                            className='stockselector')
                                           ],
                                           style={'color': '#1E1E1E'}),
                                  html.H2('Description'),
                                  html.Div(id='app3text', children='Here is a text box')
                              ]
                              ),  # Define the left element
                     html.Div(className='eight columns div-for-charts bg-grey',
                              children=[
                                  html.H2('Top5_different years'),
                                  dcc.Graph(
                                      id='gapminder2', config={'displayModeBar': True}
                                  )
                              ])  # Define the right element
                 ])
    ])

app4.layout = html.Div(
    children=[
        html.Div([nav]),
        html.Div(className='row',  # Define the row element
                 children=[
                     html.Div(className='four columns div-user-controls',
                              children=[
                                  html.H2('Description'),
                                  html.Div(id='app4text', children='Here is a text box')
                              ]
                              ),  # Define the left element
                     html.Div(className='eight columns div-for-charts bg-grey',
                              children=[
                                  html.H2('Efficiency'),
                                  html.Img(src=update_app4())
                              ])  # Define the right element
                 ])
    ])

app5.layout = html.Div(
    children=[
        html.Div([nav]),
        html.Div(className='row',  # Define the row element
                 children=[
                     html.Div(className='four columns div-user-controls',
                              children=[
                                  html.H2('Years options'),
                                  html.Div(className='div-for-dropdown',
                                           children=[
                                               dcc.Dropdown(id='years',
                                                            options=get_options(
                                                                ['2015', '2016', '2017', '2018', '2019']),
                                                            multi=False,
                                                            value='2015',
                                                            style={'backgroundColor': '#1E1E1E'},
                                                            className='stockselector'),
                                               dcc.Dropdown(id='names',
                                                            options='',
                                                            multi=False,
                                                            value='Dallas Mavericks',
                                                            style={'backgroundColor': '#1E1E1E'},
                                                            className='stockselector')
                                           ],
                                           style={'color': '#1E1E1E'}),
                                  html.H2('Description'),
                                  html.Div(id='app5text', children='Here is a text box')
                              ]
                              ),  # Define the left element
                     html.Div(className='eight columns div-for-charts bg-grey',
                              children=[
                                  html.H2('2D Score Efficiency'),
                                  DataTable(
                                    id="gapminder4",
                                    columns=[{'id': c, 'name': nameList[c]} for c in
                                              ['PLAYER_NAME', 'TEAM_NAME', 'total_poss',
                                              'Similarity Score', 'Complement Score']],
                                    page_size=10,
                                    style_header={
                                        'backgroundColor': 'white',
                                        'fontWeight': 'bold',
                                        'textAlign': 'center',
                                        'color': 'black'
                                    },
                                    style_cell={'padding': '5px',
                                                'backgroundColor': 'white',
                                                'fontWeight': 'bold',
                                                'textAlign': 'center',
                                                'color': 'black',
                                                'width': '60px'
                                    },
                                    editable=True,
                                    filter_action="native",
                                    sort_action="native",
                                    sort_mode="multi",
                                    column_selectable="single",
                                    row_selectable="multi",
                                    row_deletable=True,
                                    selected_columns=[],
                                    selected_rows=[],
                                    page_action="native",
                                    page_current=0,
                                    style_table = {'overflowX': 'auto', 'width': '98%'}
                                  )
                              ])
                 ])
    ])

app6.layout = html.Div(
    children=[
        html.Div([nav]),
        html.Div(className='row',  # Define the row element
                 children=[
                     html.Div(className='four columns div-user-controls',
                              children=[
                                  html.H2('Years options'),
                                  html.Div(className='div-for-dropdown',
                                           children=[
                                               dcc.Dropdown(id='years',
                                                            options=get_options(
                                                                ['2015', '2016', '2017', '2018', '2019']),
                                                            multi=False,
                                                            value='2015',
                                                            style={'backgroundColor': '#1E1E1E'},
                                                            className='stockselector'),
                                               dcc.Dropdown(id='names',
                                                            options=get_options(names),
                                                            multi=False,
                                                            value='Brook Lopez',
                                                            style={'backgroundColor': '#1E1E1E'},
                                                            className='stockselector')
                                           ],
                                           style={'color': '#1E1E1E'}), html.Div()

                              ]
                              ),  # Define the left element
                     html.Div(className='eight columns div-for-charts bg-grey',
                              children=[
                                  html.H2('Pie Chart'),
                                  html.Div(children=[html.Img(id='gapminder5', src=''),
                                                     html.Img(id='playphoto', src='', alt='Not Found')]),
                                  html.Div(id='app6text', children='123')
                              ])  # Define the right element
                 ])
    ])


@app_flask.route('/')
def home():
    return flask.redirect('page1')


@app3.callback(Output('gapminder2', 'figure'), [Input('years', 'value')])
def update_app(year):
    return update_app3(year)


@app5.callback(Output('gapminder4', 'data'), [Input('years', 'value'), Input('names', 'value')])
def update_app(year, name):
    return update_app5(year, name)


@app5.callback(Output('names', 'options'), [Input('years', 'value')])
def update_options(year):
    path5 = 'data2/teams_csv/teams_' + year + '_profile_table.csv'
    df5 = pd.read_csv(path5)
    names5 = df5['TEAM_NAME']
    name_new = []
    for i in names5:
        name_new.append(i)
    return get_options(name_new)


@app6.callback(Output('gapminder5', 'src'), [Input('years', 'value'), Input('names', 'value')])
def update_app(year, name):
    return update_app6(int(year), name)


@app6.callback(Output('playphoto', 'src'), [Input('names', 'value')])
def update_app(name):
    return update_photo6(name)


@app6.callback(Output('names', 'options'), [Input('years', 'value')])
def update_options(year):
    path = "data/data_cleaned/pca_data/" + year + "_pca_table.csv"
    df = pd.read_csv(path)
    names = df['PLAYER_NAME']
    return get_options(names)


@app6.callback(Output('app6text', 'children'), [Input('years', 'value'), Input('names', 'value')])
def update_text(year, name):
    return "In year {0}, {1} performs very well!".format(year, name)


if __name__ == '__main__':
    app_flask.run(host="0.0.0.0", debug=True)
