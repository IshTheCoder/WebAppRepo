import pytest
import sys
sys.path.insert(0, '..') # insert everything from .. to path search
import os
import pandas as pd

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
            

def test_K_means():
    '''
    '''
    
    
    
def test_get_silscores():
    '''
    '''
    
    
    
def test_calculate_top5():
    '''
    '''
    
    

    
def test_top5_img():
    '''
    '''
    
    
    