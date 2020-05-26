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


def update_app1():
    final_list = ['2015', '2016', '2017', '2018', '2019']
    cluster_num = {'2015': 5, '2016': 6, '2017': 7, '2018': 8, '2019': 8}
    fig = go.Figure()
    count = 0

    for each in final_list:
        names, X, labels, _ = k_means("data/data_cleaned/pca_data/" + each + '_pca_table.csv', dim=3,
                                      cluster_num=cluster_num[each])
        count += 1
        fig.add_trace(go.Scatter3d(x=X[:, 1], y=X[:, 0], z=X[:, 2], text=names, hoverinfo='text', mode='markers',
                                   marker=dict(color=labels), visible=False, name="Player Clusters for " + each))
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
            title={"text": "Scoring Clusters Per Year"}
        )
    return fig


def update_app2(year):
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
    x_1, y_1, names = scatter_plot_in("data/data_cleaned/poss_ppp_data/poss" + year + '.csv')
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
                template='plotly_dark'
            )
    }

    return figure


def update_app3(year):
    category_names = ["Iso", "Tra", "PRB", "PRR", "Pos", "Spo", "Han", "Cut", "Off", "OffR", "Misc"]
    names, _, _, distance = k_means("data/data_cleaned/pca_data/" + year + '_pca_table.csv', 3, 8)
    results = top5_img(distance, names, int(year))
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
    fig.update_layout(autosize=True, width=900, height=1200, barmode='stack')
    return fig


def update_app4():
    return plot_most_effi_figure("data/data_cleaned/poss_ppp_data")

def update_app6(year, name):
    return draw_pie_chart(name, int(year))
