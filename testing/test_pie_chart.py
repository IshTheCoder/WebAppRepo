import pytest
import sys
sys.path.insert(0, '..')



def test_pie_chart():
    '''
    '''
    from pie_chart import draw_pie_chart
    uri=draw_pie_chart('James Harden', 2015)
    assert isinstance(uri,str)
