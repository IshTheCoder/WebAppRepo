import pytest
import sys
sys.path.append('../') # insert everything from .. to path search
from pie_chart import draw_pie_chart

def test_draw_pie_chart():
    uri=draw_pie_chart('James Hardon',2015)
    assert isinstance(uri, str)