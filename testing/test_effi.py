'''
This folder tests all functions in effi.py
'''
import pytest
import sys
sys.path.insert(0, '..') # insert everything from .. to path search
import os
from effi import *
import collections


def test_get_plot_data():
    '''
    '''
    aggr_data=  '../data/data_cleaned/poss_ppp_data/'
    plot_data = get_plot_data(aggr_data)
    assert isinstance(plot_data, collections.defaultdict)


def test_plot_most_effi_figure():
    '''
    '''
    aggr_data=  '../data/data_cleaned/poss_ppp_data/'
    uri = plot_most_effi_figure(aggr_data, './testresults')
    assert isinstance(uri, str)


