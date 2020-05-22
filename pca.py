import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
from sklearn.decomposition import PCA
import plotly.graph_objects as go
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

def k_means(fname, dim=3, cluster_num=5):
    '''
    Function to cluster the data into cluster_num groups and visualize them in a 3D space
    :param fname: the path of the pca_table file
    :param dim: the number of dimensions we want to use
    :param cluster_num: the number of clusters we want to cluster them
    :return: NONE
    '''
    assert isinstance(fname, str)
    data, names = pca_processing(fname, dim)
    X = np.array(data)
    k_means = KMeans(n_clusters=cluster_num).fit(X)
    labels = k_means.labels_

    return names, X, labels

def get_silscores(fname, dim=3):
    best=0
    final_clus=0
    for cluster_num in range(5,9):
        data, names = pca_processing(fname, dim)
        X = np.array(data)
        k_means = KMeans(n_clusters=cluster_num).fit(X)
        labels = k_means.labels_
        silhouette_avg = silhouette_score(X, labels)
        if silhouette_avg >= best:
            best = silhouette_avg
            final_clus= cluster_num

    return best, final_clus