import pytest
import sys
sys.path.insert(0, '..') # insert everything from .. to path search
import os
import pandas as pd
import numpy as np
from sim_com import *


def test_sim_com():
    '''
    '''
    df1 = pd.read_csv('../data2/updated_players_csv/2019_profile_table.csv')
    df2 = pd.read_csv('../data2/teams_csv/teams_2019_profile_table.csv')
    sim_val =  sim_com(df1,df2,'Dallas Mavericks', num_poss = 200)
    assert isinstance(sim_val, pd.DataFrame)