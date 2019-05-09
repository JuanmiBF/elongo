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
        title='Coal/petroleum electricity generation comparison',
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
        title='Electricity generation with coal',
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


def comparison(request):
    if request.method == 'POST':
        form = ComparisonForm(request.POST)
        if form.is_valid():
            graph = generate_graph(form.cleaned_data['city'], form.cleaned_data['field_1'],
                                       form.cleaned_data['field_2'])

            return render(request, 'comparison_form.html', {'form': form, 'graph': graph})

    else:
        form = ComparisonForm()
    return render(request, 'comparison_form.html', {'form': form})


def generate_graph(city, field_1, field_2):
    electric_data = ElectricData.objects.filter(city=city).order_by('year')

    x = [datetime.datetime(year=ed.year, month=1, day=1) for ed in electric_data]
    field_1_y = [getattr(ed, field_1) for ed in electric_data]

    field_1_scatter = go.Scatter(
        x=x,
        y=field_1_y,
        name=field_1.replace("_", " ").capitalize(),
        line=dict(color='#17BECF'),
        opacity=0.8)

    if not field_2:
        layout = dict(
            title="{} electricity generation in the city of {}".format(field_1.replace("_", " ").capitalize(), city),
            xaxis=dict(
                title='Year',
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
            ),
            yaxis=dict(title='GWh')
        )
        fig = dict(data=[field_1_scatter], layout=layout)
        graph = opy.plot(fig, auto_open=False, output_type='div')
    else:
        field_2_y = [getattr(ed, field_2) for ed in electric_data]

        field_2_scatter = go.Scatter(
            x=x,
            y=field_2_y,
            name=field_2.replace("_", " ").capitalize(),
            line=dict(color='#7F7F7F'),
            opacity=0.8)

        data = [field_1_scatter, field_2_scatter]

        layout = dict(
            title='{}/{} electricity generation comparison in the city of {}'.format(field_1.replace("_", " ").capitalize(), field_2.replace("_", " "), city),
            xaxis=dict(
                title='Year',
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
            ),
            yaxis=dict(title='GWh')
        )

        fig = dict(data=data, layout=layout)
        graph = opy.plot(fig, auto_open=False, output_type='div')

    return graph

def city_details(request,city_id):
    if city_id:
        city = City.objects.filter(id=city_id)
        list_electric_data = ElectricData.objects.filter(city=city)
        average_total_consume = 0
        average_coal_consume=0
        average_natural_gas_consume = 0
        average_petroleum_consume = 0
        average_hydro_consume = 0
        average_nuclear_consume = 0
        average_other_consume = 0
        average_wood_consume = 0
        average_wind_consume = 0
        average_solar_consume = 0
        if len(list_electric_data)>0:
          average_total_consume = lambda x: average_total_consume + x.total,list_electric_data
          #average_total_consume =  average_total_consume + t.total for t in list_electric_data


    return render(request, 'elongoApp/listElectricData.html', {'list': list_electric_data})


@login_required()
def new_electric_data(request):
    if request.method == "POST":
        form= ElectricDataForm(request.POST)
        if form.is_valid():
            electricData = form.save(commit=False)
            electricData.save()
            return render(request, 'elongoApp/index.html')
    else:
        form = ElectricDataForm()
        return render(request, 'elongoApp/electric_data_form.html', {'form': form})

def list_electric_data(request):
    list = ElectricData.objects.all().order_by('city','year')
    return render(request, 'elongoApp/listElectricData.html', {'list': list})


