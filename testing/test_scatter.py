import pytest
import sys
import os
sys.path.insert(0, '../') # insert everything from .. to path search
from src.scatter import *
import plotly.graph_objs as go

def test_create_slider_scatter():
    os.chdir('../')
    fig=create_slider_scatter(['2015', '2016', '2017', '2018', '2019'], 'Points Per Possession vs Possessions',
                                 'PPP', 'Possessions')
    assert isinstance(fig,go.Figure)
    os.chdir(os.getcwd() + '/testing')
