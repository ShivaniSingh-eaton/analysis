from test_github_release.main import value_main
from test_github_release.folder_1.d import a_value
import pandas as pd
from pathlib import Path
import os
def test_main():
    '''
    This function tests main function
    '''

    x = value_main(y=1,x=1)
    assert x == 27

def test_a_value():
    '''
    This function tests main function
    '''

    x = a_value()
    assert x == 2

def test_1_value():
    '''
    This function tests main function
    '''

    print(os.path.join(os.path.dirname(__file__),"ip"))
    path = os.path.join(os.path.dirname(__file__),"ip")
    filename="test1.csv"
    print(os.path.join(path, filename))
    df1= pd.read_csv(os.path.join(path, filename))
    path = os.path.join(Path(__file__).parent.parent,"reference")
    print(path)
    filename="test2.csv"
    path = os.path.join(path, filename)
    print(path)
    df2= pd.read_csv(path)
    assert not df1.empty
    assert not df2.empty
