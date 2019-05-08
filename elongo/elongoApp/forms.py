from django import forms

from .models import *

class ElectricDataForm(forms.ModelForm):

    class Meta:
        model = ElectricData
        fields = ('year', 'coal','natural_gas', 'petroleum','conv_hydro', 'ps_hydro','nuclear', 'net_imports',
                  'other', 'waste', 'landfill_gas', 'wood','wind', 'solar', 'total')


class CityForm(forms.ModelForm):

    class Meta:
        model = City
        fields = ('name','population's)