from django import forms

from .models import *


class ElectricDataForm(forms.ModelForm):

    class Meta:
        model = ElectricData
        city = forms.ModelChoiceField(queryset=City.objects.all())
        fields = ('year', 'coal','natural_gas', 'petroleum','conv_hydro', 'ps_hydro','nuclear', 'net_imports',
                  'other', 'waste', 'landfill_gas', 'wood','wind', 'solar', 'total','city','population')


class CityForm(forms.ModelForm):

    class Meta:
        model = City
        fields = ('name','country','continent')

class ComparisonForm(forms.Form):
	CHOICES = ((None, '----------'), ('coal', 'Coal'), ('natural_gas', 'Natural gas'),
			   ('petroleum', 'Petroleum'), ('conv_hydro', 'Conv hydro'),
			   ('ps_hydro', 'Ps hydro'), ('nuclear', 'Nuclear'), ('net_imports', 'Net imports'),
			   ('other', 'Other'),
			   ('waste', 'Waste'), ('landfill_gas', 'Landfill gas'), ('wood', 'Wood'), ('wind', 'Wind'),
			   ('solar', 'Solar'),
			   ('total', 'Total'))

	city = forms.ModelChoiceField(queryset=City.objects.all(), required=True)
	field_1 = forms.ChoiceField(choices=CHOICES, required=True)
	field_2 = forms.ChoiceField(choices=CHOICES, required=False)
