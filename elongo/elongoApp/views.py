from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline as opy
from .forms import *

import datetime

# Create your views here.


def index(request):

    electric_data = ElectricData.objects.all().order_by('year')

    x = [datetime.datetime(year=ed.year, month=1, day=1) for ed in electric_data]
    coal_y = [ed.coal for ed in electric_data]
    petroleum_y = [ed.petroleum for ed in electric_data]

    coal = go.Scatter(
        x=x,
        y=coal_y,
        name="Coal",
        line=dict(color='#17BECF'),
        opacity=0.8)

    petroleum = go.Scatter(
        x=x,
        y=petroleum_y,
        name="Petroleum",
        line=dict(color='#7F7F7F'),
        opacity=0.8)

    data = [coal, petroleum]

    layoutComp = dict(
        title='Comparison coal/petroleum',
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                         label='1y',
                         step='year',
                         stepmode='backward'),
                    dict(count=5,
                         label='5y',
                         step='year',
                         stepmode='backward'),
                    dict(step='all')
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
            type='date'
        )
    )


    figComp = dict(data=data, layout=layoutComp)
    divComp = opy.plot(figComp, auto_open=False, output_type='div')


    # This is for not comparing grapth
    layout = dict(
        title='Coal',
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                         label='1y',
                         step='year',
                         stepmode='backward'),
                    dict(count=5,
                         label='5y',
                         step='year',
                         stepmode='backward'),
                    dict(step='all')
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
            type='date'
        )
    )
    fig = dict(data=[coal], layout=layout)
    div = opy.plot(fig, auto_open=False, output_type='div')
    # py.iplot(fig)

    return render(request, 'elongoApp/index.html', {'graphComp': divComp, 'graph': div})


def to_unix_time(dt):
    epoch = datetime.datetime.utcfromtimestamp(0)
    return (dt - epoch).total_seconds() * 1000


def new_city(request):
    if request.method == "POST":
        form= CityForm(request.POST)
        if form.is_valid():
            city = form.save(commit=False)
            city.save()
            return render(request, 'elongoApp/index.html')
    else:
        form = CityForm()
        return render(request, 'elongoApp/city_form.html', {'form': form})

def list_city(request):
    list = City.objects.all()
    return render(request, 'elongoApp/listCity.html', {'list': list})

