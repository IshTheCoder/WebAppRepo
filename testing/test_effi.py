'''
This folder tests all functions in effi.py
'''
import sys
sys.path.insert(0, '..')
import pytest
import os

import collections



def test_get_plot_data():
    '''
    '''
    from effi import get_plot_data
    aggr_data=  '/data/data_cleaned/poss_ppp_data/'
    plot_data = get_plot_data(aggr_data)
    assert isinstance(plot_data, collections.defaultdict)


def test_plot_most_effi_figure():
    '''
    '''
    from effi import plot_most_effi_figure
    aggr_data=  '/data/data_cleaned/poss_ppp_data/'
    uri = plot_most_effi_figure(aggr_data, 'testing/testresults')
    assert isinstance(uri, str)


