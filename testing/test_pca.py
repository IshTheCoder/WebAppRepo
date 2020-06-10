import pytest
import sys
sys.path.insert(0, '..') # insert everything from .. to path search
import os
import pandas as pd
import numpy as np
from pca import *

def test_pca_processing():
    '''This function tests pca_processing which reads the different years data and reduces 
    the dimension of the players based on their POSS_PCT
    '''
    fname = '../data/data_cleaned/pca_data/'
    frame_list = ['2015_pca_table.csv', '2016_pca_table.csv','2017_pca_table.csv','2018_pca_table.csv','2019_pca_table.csv']
    for frame in frame_list:
        path = os.path.join(fname, frame)
        assert os.path.isfile(path) # checking if all inputs to be given exist
    data, players = pca_processing(path)
    assert isinstance(data, pd.DataFrame) #check for correct format
    assert isinstance(players, pd.Series)
    assert players.is_unique #check if all names are unique
    assert len(data) == len(players)
            

def test_k_means():
    '''This function tests k-means clustering for corner cases
    '''
    fname = '../data/data_cleaned/pca_data/'
    frame_list = ['2015_pca_table.csv', '2016_pca_table.csv','2017_pca_table.csv','2018_pca_table.csv','2019_pca_table.csv']
    for frame in frame_list:
        path = os.path.join(fname, frame)
        assert os.path.isfile(path) # checking if all inputs to be given exist
    names, X, labels, distance = k_means(path)
    assert isinstance(names, pd.Series) #check for correct format
    assert isinstance(X, np.ndarray)
    assert isinstance(labels, np.ndarray)
    assert isinstance(distance, np.ndarray)
    assert len(names) == len(X) == len(distance) == len(labels)
  
    
    
def test_get_silscores():
    '''This function tests the get silhoutte scores function
    '''
    fname = '../data/data_cleaned/pca_data/'
    frame_list = ['2015_pca_table.csv', '2016_pca_table.csv','2017_pca_table.csv','2018_pca_table.csv','2019_pca_table.csv']
    for frame in frame_list:
        path = os.path.join(fname, frame)
        assert os.path.isfile(path) # checking if all inputs to be given exist
    best, final_clus = get_silscores(path)
    assert type(best) == np.float64
    assert type(final_clus) == int
 
    
def test_calculate_top5():
    ''' Test function for calculate_top5 which finds the top5 players who are the most closest to the k-means's cluster center
    '''
    fname = '../data/data_cleaned/pca_data/'
    frame_list = ['2015_pca_table.csv', '2016_pca_table.csv','2017_pca_table.csv','2018_pca_table.csv','2019_pca_table.csv']
    for frame in frame_list:
        path = os.path.join(fname, frame)
        assert os.path.isfile(path) # checking if all inputs to be given exist
    names, X, labels, distance = k_means(path)
    assert isinstance(names, pd.Series) #check for correct format
    assert isinstance(X, np.ndarray)
    assert isinstance(labels, np.ndarray)
    assert isinstance(distance, np.ndarray)
    assert len(names) == len(X) == len(distance) == len(labels)
    
    top5_name = calculate_top5(distance, names)
    assert isinstance(top5_name, list)
    assert all(isinstance(i, list) for i in top5_name)
    assert all(len(set(i)) == len(i) for i in top5_name) # all unique
    

    
def test_top5_img():
    '''
    '''
    year = 2019
    cluster_num = 5
    assert 2015 <= year <= 2019
    fname = '../data/data_cleaned/pca_data/'
    frame_list = ['2015_pca_table.csv', '2016_pca_table.csv','2017_pca_table.csv','2018_pca_table.csv','2019_pca_table.csv']
    for frame in frame_list:
        path = os.path.join(fname, frame)
        assert os.path.isfile(path) # checking if all inputs to be given exist
    names, X, labels, distance = k_means(path)
    assert isinstance(names, pd.Series) #check for correct format
    assert isinstance(X, np.ndarray)
    assert isinstance(labels, np.ndarray)
    assert isinstance(distance, np.ndarray)
    assert len(names) == len(X) == len(distance) == len(labels)
    
    result = top5_img(distance, names, year, cluster_num, test = True)
    assert isinstance(result, dict)