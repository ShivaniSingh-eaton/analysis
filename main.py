from test_github_release.a import a_value
from test_github_release.b import b_value
from test_github_release.c import c_value
from test_github_release.d import d_value
from test_github_release.e import e_value
from test_github_release.f import f_value

def g_value():
    return 6

def value_main(y,x=1):
    return a_value()+b_value() +c_value() + d_value() + e_value() + f_value() + g_value()
