import pytest
import sys
sys.path.append('../') # insert everything from .. to path search
import os
import pandas as pd
import numpy as np
import dash_bootstrap_components
from navbar import *

def test_Navbar():
    '''
    '''
    navbar = Navbar()
    assert navbar
    assert isinstance(navbar, dash_bootstrap_components._components.NavbarSimple)