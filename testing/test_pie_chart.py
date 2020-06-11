import pytest
import sys
import os
sys.path.insert(0, '../') # insert everything from .. to path search
from src.pie_chart import draw_pie_chart

def test_draw_pie_chart():
    os.chdir('../')
    print(os.getcwd())
    uri=draw_pie_chart('James Harden',2015)
    os.chdir(os.getcwd()+'/testing')
    assert isinstance(uri, str)