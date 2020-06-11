import pytest
import sys
sys.path.insert(0, '..')
import os
import pandas as pd
import numpy as np
import dash_bootstrap_components



def test_Navbar():
    '''
    '''
    from navbar import Navbar
    navbar = Navbar()
    assert navbar
    assert isinstance(navbar, dash_bootstrap_components._components.NavbarSimple)