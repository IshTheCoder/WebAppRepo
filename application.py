from dash.dependencies import Input, Output
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go
from pca import k_means
from scatter import  scatter_plot_in
from navbar import Navbar
import dash_bootstrap_components as dbc
import flask

def get_options(list_stocks):
    dict_list = []
    for i in list_stocks:
        dict_list.append({'label': i, 'value': i})

    return dict_list

app_flask=flask.Flask(__name__)

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.UNITED], server=app_flask,url_base_pathname='/page1/')

app2 = dash.Dash(__name__, external_stylesheets = [dbc.themes.UNITED],server = app_flask, url_base_pathname='/page2/')

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

@app_flask.route('/')
def home():
    return flask.redirect('page1')

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





@app.callback(Output('gapminder', 'figure'),[Input('years', 'value')])
def update_gapminder(selected_dropdown_value):

    
    final_list=['2015','2016','2017','2018','2019']
    cluster_num = {'2015': 5, '2016':6, '2017':7, '2018':8, '2019':8}
    fig = go.Figure()
    count = 0

    for each in final_list:

      names, X, labels = k_means("data/data_cleaned/pca_data/"+each+'_pca_table.csv', dim=3, cluster_num=cluster_num[each])
      print("Test")
      count+= 1
      fig.add_trace(go.Scatter3d(x=X[:, 1], y=X[:, 0], z=X[:, 2], text = names, hoverinfo = 'text', mode='markers', marker=dict(color=labels), visible=False, name="Player Clusters for " + each))
      steps = []
      for i in range(len(fig.data)):
          step = dict(
              method="restyle",
              args=["visible", [False] * len(fig.data)],
              label='Year ' + str(i + 2015)

          )
          step["args"][1][i] = True  # Toggle i'th trace to "visible"
          steps.append(step)
      sliders = [dict(active=5,
        currentvalue={"prefix": "Year: "},
        pad={"t": 5},
        steps=steps)]
      start_index = 2015
      fig.update_layout(
        sliders=sliders,
        #title = "9 Cluster classification of players based on Scoring Styles"
        title={"text": "Scoring Clusters Per Year"}
        )


      #fig.show()


      #plotly.offline.plot(fig, filename='Cluster_final.html')




    # figure = {
    #     'data': [
    #         go.Scatter3d(x=X[:, 1],
    #                      y=X[:, 0],
    #                      z=X[:, 2],
    #                      text=names,
    #                      hoverinfo='text',
    #                      mode='markers',
    #                      marker=dict(color=labels)
    #                      )
    #     ],
    #     'layout':
    #         dict(
    #             title='Scoring Clusters Per Year',
    #             xaxis={'title': 'x'},
    #             yaxis={'title': 'y'},
    #             zaxis={'title': 'z'},
    #             hovermode='closest',
    #             template = 'plotly_dark',
    #         )
    # }

    return fig

@app2.callback(Output('gapminder1', 'figure'), [Input('years', 'value')])
def update_gapminder(selected_dropdown_value):
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


if __name__ == '__main__':
    app_flask.run(host="0.0.0.0")
