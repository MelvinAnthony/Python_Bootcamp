from ipywidgets import interact,interactive,fixed
import ipywidgets as widgets

def fun(x,y):
    yield x
    yield y

interact(fun,x=10,y=10)
