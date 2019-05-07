from django.shortcuts import render
from .models import *
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline as opy

import datetime

# Create your views here.


def index(request):
    x = [datetime.datetime(year=2013, month=10, day=4),
         datetime.datetime(year=2013, month=11, day=5),
         datetime.datetime(year=2013, month=12, day=6)]
    data = [go.Scatter(
        x=x,
        y=[1, 3, 6])]

    layout = go.Layout(xaxis=dict(
        range=[to_unix_time(datetime.datetime(2013, 10, 17)),
               to_unix_time(datetime.datetime(2013, 11, 20))]
    ))

    fig = go.Figure(data=data, layout=layout)
    div = opy.plot(fig, auto_open=False, output_type='div')
    # py.iplot(fig)

    return render(request, 'elongoApp/test.html', {'graph': div})


def to_unix_time(dt):
    epoch = datetime.datetime.utcfromtimestamp(0)
    return (dt - epoch).total_seconds() * 1000
