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

def get_options(list_stocks):
    dict_list = []
    for i in list_stocks:
        dict_list.append({'label': i, 'value': i})

    return dict_list
matplotlib.use('agg')

path = "data/data_cleaned/pca_data/2015_pca_table.csv"
df = pd.read_csv(path)
names= df['PLAYER_NAME']

app_flask=flask.Flask(__name__)

app  = dash.Dash(__name__, external_stylesheets = [dbc.themes.UNITED],server = app_flask, url_base_pathname='/page1/')

app2 = dash.Dash(__name__, external_stylesheets = [dbc.themes.UNITED],server = app_flask, url_base_pathname='/page2/')

app3 = dash.Dash(__name__, external_stylesheets = [dbc.themes.UNITED],server = app_flask, url_base_pathname='/page3/')

app4 = dash.Dash(__name__, external_stylesheets = [dbc.themes.UNITED],server = app_flask, url_base_pathname='/page4/')

app5 = dash.Dash(__name__, external_stylesheets = [dbc.themes.UNITED],server = app_flask, url_base_pathname='/page5/')

app6 = dash.Dash(__name__, external_stylesheets = [dbc.themes.UNITED],server = app_flask, url_base_pathname='/page6/')

nav = Navbar()

app.layout = html.Div(
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
                                                            options=get_options(['2015', '2016', '2017', '2018', '2019']),
                                                            multi=False,
                                                            value='2015',
                                                            style={'backgroundColor': '#1E1E1E'},
                                                            className='stockselector')
                                           ],
                                           style={'color': '#1E1E1E'})
                              ]
                              ),  # Define the left element
                     html.Div(className='eight columns div-for-charts bg-grey',
                              children=[
                                  html.H2('ECE229-PCA'),
                                  dcc.Graph(
                                      id='gapminder', config={'displayModeBar': True}
                                  )
                                # Sniphx.H2('2D scatter plot'),
                                # dcc.Graph(
                                #     id='gapminder1', config={'displayModeBar': False}
                                # )
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
                                  html.H2('Years options'),
                                  html.Div(className='div-for-dropdown',
                                           children=[
                                               dcc.Dropdown(id='years',
                                                            options=get_options(['2015', '2016', '2017', '2018', '2019']),
                                                            multi=False,
                                                            value='2015',
                                                            style={'backgroundColor': '#1E1E1E'},
                                                            className='stockselector')
                                           ],
                                           style={'color': '#1E1E1E'})
                              ]
                              ),  # Define the left element
                     html.Div(className='eight columns div-for-charts bg-grey',
                              children=[
                                  # Sniphx.H2('ECE229-PCA'),
                                  # dcc.Graph(
                                  #     id='gapminder', config={'displayModeBar': False}
                                  # ),
                                html.H2('2D scatter plot'),
                                dcc.Graph(
                                    id='gapminder1', config={'displayModeBar': True}
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
                                                            options=get_options(['2015', '2016', '2017', '2018', '2019']),
                                                            multi=False,
                                                            value='2015',
                                                            style={'backgroundColor': '#1E1E1E'},
                                                            className='stockselector')
                                           ],
                                           style={'color': '#1E1E1E'})
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
                                  html.H2('Years options'),
                                  html.Div(className='div-for-dropdown',
                                           children=[
                                               dcc.Dropdown(id='years',
                                                            options=get_options(['2015', '2016', '2017', '2018', '2019']),
                                                            multi=False,
                                                            value='2015',
                                                            style={'backgroundColor': '#1E1E1E'},
                                                            className='stockselector')
                                           ],
                                           style={'color': '#1E1E1E'})
                              ]
                              ),  # Define the left element
                     html.Div(className='eight columns div-for-charts bg-grey',
                              children=[
                                  html.H2('3D-cluster'),
                                  dcc.Graph(
                                      id='gapminder3', config={'displayModeBar': True}
                                  )
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
                                                            options=get_options(['2015', '2016', '2017', '2018', '2019']),
                                                            multi=False,
                                                            value='2015',
                                                            style={'backgroundColor': '#1E1E1E'},
                                                            className='stockselector')
                                           ],
                                           style={'color': '#1E1E1E'})
                              ]
                              ),  # Define the left element
                     html.Div(className='eight columns div-for-charts bg-grey',
                              children=[
                                  html.H2('2D Score Efficiency'),
                                  dcc.Graph(
                                      id='gapminder4', config={'displayModeBar': True}
                                  )
                              ])  # Define the right element
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
                                                            options=get_options(['2015', '2016', '2017', '2018', '2019']),
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
                                           style={'color': '#1E1E1E'})
                              ]
                              ),  # Define the left element
                     html.Div(className='eight columns div-for-charts bg-grey',
                              children=[
                                  html.H2('Pie Chart'),
                                  # dcc.Graph(
                                  #     id='gapminder5', config={'displayModeBar': True}
                                  # )
                                  html.Div([html.Img(id='gapminder5',src='')])
                              ])  # Define the right element
                 ])
])



@app_flask.route('/')
def home():
    return flask.redirect('page1')


@app.callback (Output('gapminder', 'figure'), [Input('years', 'value')])
def update_app(selected_dropdown_value):
    cluster_num = {'2015': 5, '2016':6, '2017':7, '2018':8, '2019':8}
    names, X, labels,_ = k_means("data/data_cleaned/pca_data/"+selected_dropdown_value+'_pca_table.csv', dim=3, cluster_num=cluster_num[selected_dropdown_value])
    figure = {
        'data': [
            go.Scatter3d(x=X[:, 1],
                         y=X[:, 0],
                         z=X[:, 2],
                         text=names,
                         hoverinfo='text',
                         mode='markers',
                         marker=dict(color=labels)
                         )
        ],
        'layout':
            dict(
                title='Scoring Clusters Per Year',
                xaxis={'title': 'x'},
                yaxis={'title': 'y'},
                zaxis={'title': 'z'},
                hovermode='closest',
                template = 'plotly_dark',
            )
    }
    return figure

@app2.callback(Output('gapminder1', 'figure'),[Input('years', 'value')])
def update_app1(selected_dropdown_value):
    colorscale_curr = [[0.0, "rgb(165,0,38)"],
                       [0.1111111111111111, "rgb(215,48,39)"],
                       [0.2222222222222222, "rgb(244,109,67)"],
                       [0.3333333333333333, "rgb(253,174,97)"],
                       [0.4444444444444444, "rgb(254,224,144)"],
                       [0.5555555555555556, "rgb(224,243,248)"],
                       [0.6666666666666666, "rgb(171,217,233)"],
                       [0.7777777777777778, "rgb(116,173,209)"],
                       [0.8888888888888888, "rgb(69,117,180)"],
                       [1.0, "rgb(49,54,149)"]]
    colorscale_curr.reverse()
    x_1, y_1, names = scatter_plot_in("data/data_cleaned/poss_ppp_data/poss" + selected_dropdown_value + '.csv')
    figure = {
        'data': [
            go.Scatter(x=x_1,
                       y=y_1,
                       text=names,
                       hoverinfo='text',
                       mode='markers',
                       marker=dict(color=y_1,
                                   colorscale=colorscale_curr,
                                   size=12,
                                   line=dict(width=2, color='DarkSlateGrey')
                                   )
                       )
        ],
        'layout':
            dict(
                title='2-D scatter plot',
                xaxis={'title': 'Possessions'},
                yaxis={'title': 'PPP'},
                hovermode='closest',
                template = 'plotly_dark'
            )
    }

    return figure

@app3.callback(Output('gapminder2', 'figure'),[Input('years', 'value')])
def update_app(selected_dropdown_value):
    category_names = ["Iso", "Tra", "PRB", "PRR", "Pos", "Spo", "Han", "Cut", "Off", "OffR", "Misc"]
    names, _ , _, distance = k_means("data/data_cleaned/pca_data/" + selected_dropdown_value + '_pca_table.csv', 3, 8)
    results = top5_img(distance, names, int(selected_dropdown_value))
    labels = list(results.keys())
    new_labels = []
    start = " "
    for i in range(len(labels)):
        new_labels.append(labels[i])
        if i % 5 == 4:
            new_labels.append(start)
            start += " "
    labels = new_labels
    data = np.array(list(results.values()))
    new_data = []
    for i in range(len(data)):
        new_data.append(data[i])
        if i % 5 == 4:
            new_data.append(np.zeros(shape=data[0].shape))
    data = np.array(new_data)

    data_cum = data.cumsum(axis=1)
    category_colors = plt.get_cmap('RdYlGn')(
        np.linspace(0.15, 0.85, data.shape[1]))

    fig = go.Figure()
    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        color = tuple([color[i] * 255 for i in range(3)] + [1])
        starts = data_cum[:, i] - widths
        fig.add_trace(go.Bar(
            y=labels,
            x=widths,
            name=colname,
            orientation='h',
            marker=dict(
                color='rgba' + str(color),
                line=dict(color='rgba' + str(color), width=1.5)
            )
        )
        )
    fig.update_layout(autosize=True, width=900, height=600, barmode='stack')
    return fig

@app4.callback(Output('gapminder3', 'figure'),[Input('years', 'value')])
def update_app(selected_dropdown_value):
    cluster_num = {'2015': 5, '2016':6, '2017':7, '2018':8, '2019':8}
    names, X, labels = k_means("data/data_cleaned/pca_data/"+selected_dropdown_value+'_pca_table.csv', dim=3, cluster_num=cluster_num[selected_dropdown_value])
    figure = {
        'data': [
            go.Scatter3d(x=X[:, 1],
                         y=X[:, 0],
                         z=X[:, 2],
                         text=names,
                         hoverinfo='text',
                         mode='markers',
                         marker=dict(color=labels)
                         )
        ],
        'layout':
            dict(
                title='Scoring Clusters Per Year',
                xaxis={'title': 'x'},
                yaxis={'title': 'y'},
                zaxis={'title': 'z'},
                hovermode='closest',
                template = 'plotly_dark',
            )
    }
    return figure

@app5.callback(Output('gapminder4', 'figure'),[Input('years', 'value')])
def update_app(selected_dropdown_value):
    cluster_num = {'2015': 5, '2016':6, '2017':7, '2018':8, '2019':8}
    names, X, labels = k_means("data/data_cleaned/pca_data/"+selected_dropdown_value+'_pca_table.csv', dim=3, cluster_num=cluster_num[selected_dropdown_value])
    figure = {
        'data': [
            go.Scatter3d(x=X[:, 1],
                         y=X[:, 0],
                         z=X[:, 2],
                         text=names,
                         hoverinfo='text',
                         mode='markers',
                         marker=dict(color=labels)
                         )
        ],
        'layout':
            dict(
                title='Scoring Clusters Per Year',
                xaxis={'title': 'x'},
                yaxis={'title': 'y'},
                zaxis={'title': 'z'},
                hovermode='closest',
                template = 'plotly_dark',
            )
    }
    return figure

@app6.callback(Output('gapminder5', 'src'),[Input('years', 'value'),Input('names', 'value')])
def update_app(year,name):
    return draw_pie_chart(name, int(year))


if __name__ == '__main__':
    app_flask.run(host="0.0.0.0",debug=True)
