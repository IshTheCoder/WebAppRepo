import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import plotly
import plotly.graph_objects as go
from plotly.tools import mpl_to_plotly
from dash.dependencies import Input, Output

import io
from flask import Flask
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

def pca_processing(fname, n_comp=3):
    '''
    Function to decrease the dimension of the players based on their POSS_PCT
    :param fname: the path of the pca_table file
    :param n_comp: the number of main components we want to use
    :return: data after pca with dimension n*n_comp; player names
    '''
    df = pd.read_csv(fname)
    kept_cols = [
        col for col in df.columns if col.endswith("freq")
    ]
    kept_cols.append("PLAYER_NAME")
    kept_cols.reverse()
    df = df[kept_cols]

    player_name = df["PLAYER_NAME"]
    data_org = df.iloc[:, 2:]
    pca = PCA(n_components=n_comp)
    pca.fit(data_org)
    data_pca = data_org @ pca.components_.T
    assert len(data_pca) == len(player_name)

    return data_pca, player_name


def k_means(fname, dim=3, cluster_num=5, show_img=False):
    '''
    Function to cluster the data into cluster_num groups and visualize them in a 3D space
    :param fname: the path of the pca_table file
    :param dim: the number of dimensions we want to use
    :param cluster_num: the number of clusters we want to cluster them
    :param show_img: show k-means image or not
    :return: NONE
    '''
    assert isinstance(fname, str)
    data, names = pca_processing(fname, dim)
    X = np.array(data)
    k_means = KMeans(n_clusters=cluster_num).fit(X)
    labels = k_means.labels_
    distance = k_means.transform(X)
    return names, X, labels, distance

def calculate_top5(distance, names):
    '''
    Function to find the top5 players who are the most closest to the k-means's cluster center
    :param distance: Distance of each player to the clusters
    :param names: names of each player
    :return: top5 names of each clusters
    '''
    dim = len(distance[0])
    result = np.zeros((dim, 5))
    top5_name = []
    for i in range(dim):
        temp = []
        curr = np.array(distance[:, i])
        min_5 = curr.argsort()[:5]
        result[i, :] = min_5
        for index in min_5:
            temp.append(names[index])
        top5_name.append(temp)
    return top5_name

def top5_img(distance, names, year):
    '''
    :param distance: distance of player to kmeans center
    :param names: player names
    :param year: year
    :return: dictionary of player names and their play type
    '''
    assert 2015 <= year <= 2019
    top5names = calculate_top5(distance, names)
    path = "data/data_cleaned/pca_data/" + str(year) + "_pca_table.csv"
    df = pd.read_csv(path)
    data_per_player = np.zeros((1, 11))
    for i in range(len(top5names)):
        for j in range(len(top5names[i])):
            new_df = df[df['PLAYER_NAME'] == top5names[i][j]]
            data = new_df[
                ["iso_freq", "tr_freq", "prb_freq", "prr_freq", "pu_freq", "su_freq", "ho_freq", "cut_freq", "os_freq",
                 "putback_freq", "misc_freq"]]
            data = data.values.tolist()
            data = np.array(data)[0]
            data_per_player = np.vstack((data_per_player, data))
    data_per_player = data_per_player[1:,:]
    data_per_player = data_per_player / data_per_player.sum(axis=1, keepdims=True)
    # print(data_per_player.shape)
    result = {}
    for i in range(8):
        for j in range(5):
            result[top5names[i][j]] = data_per_player[i * 5 + j, :]
    return result



def get_options(list_stocks):
    dict_list = []
    for i in list_stocks:
        dict_list.append({'label': i, 'value': i})

    return dict_list



app = dash.Dash(__name__)

app.layout = html.Div(children=[
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
                                    style={'color': '#1E1E1E'}
                            )
                        ]
                ),  # Define the left element
                html.Div(className='eight columns div-for-charts bg-grey',
                        children=[
                            html.H2('Matplotlib Figure'),
                            dcc.Graph(
                                id='gapminder', config={'displayModeBar': True}
                            )
                        ]
                )   # Define the right element
            ]
    )
])



@app.callback(Output('gapminder', 'figure'),[Input('years', 'value')])
def update_gapminder(selected_dropdown_value):
    category_names = ["Iso", "Tra", "PRB", "PRR", "Pos", "Spo", "Han", "Cut", "Off", "OffR", "Misc"]
    names, _, distance = k_means("data/data_cleaned/pca_data/"+selected_dropdown_value+'_pca_table.csv', 3, 8)
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
        color = tuple([color[i]*255 for i in range(3)] + [1])
        starts = data_cum[:, i] - widths
        fig.add_trace(go.Bar(
                        y=labels,
                        x=widths,
                        name=colname,
                        orientation='h',
                        marker=dict(
                            color='rgba'+str(color),
                            line=dict(color='rgba'+str(color), width=1.5)
                        )
                    )
        )
    fig.update_layout(autosize=False, width=1400, height=1200, barmode='stack')
    return fig


application = app.server
if __name__ == '__main__':
    application.run(host="0.0.0.0", debug = True)