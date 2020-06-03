import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
from sklearn.decomposition import PCA
import plotly.graph_objects as go
from sklearn.metrics import silhouette_score

def pca_all(fname, n_comp =3):
    """
    Function to decrease the dimension of the players based on their POSS_PCT
    :param fname: the path of the pca_table file
    :param n_comp: the number of main components we want to use
    :return: data after pca with dimension n*n_comp; player names, the pca dimensions correspond to a pca fit across all years
    """

    df_list = []
    frame_list = ['2015_pca_table.csv', '2016_pca_table.csv','2017_pca_table.csv','2018_pca_table.csv','2019_pca_table.csv']

    for each in frame_list:
        df_new = pd.read_csv('data/data_cleaned/pca_data/'+each)
        df_list.append(df_new)



    df_concat = pd.concat(df_list)
    #print(df_concat)


    df = pd.read_csv(fname)
    kept_cols = [
        col for col in df.columns if col.endswith("freq")
    ]
    kept_cols.append("PLAYER_NAME")
    kept_cols.reverse()
    df = df[kept_cols]
    df_concat = df_concat[kept_cols]


    player_name = df["PLAYER_NAME"]

    data_org = df_concat.iloc[:, 2:]
    data_test = df.iloc[:, 2:]

    pca = PCA(n_components=n_comp)
    pca.fit(data_org)
    data_pca = data_test @ pca.components_.T
    assert len(data_pca) == len(player_name)

    return data_pca, player_name



def tests(year = 2018):
    return (pca_all("data/data_cleaned/pca_data/" +str(year) +"_pca_table.csv"))


#print(tests())
