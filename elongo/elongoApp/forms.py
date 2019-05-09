from django import forms

from .models import *


class ElectricDataForm(forms.Form):
	city = forms.ModelChoiceField(queryset=City.objects.all(), required=True)
	year = forms.IntegerField(label='Year', min_value=0, required=True)
	population = forms.IntegerField(label='Population', min_value=0, required=True)
	coal = forms.IntegerField(label='Coal (GWh)', min_value=0, required=True)
	natural_gas = forms.IntegerField(label='Natural gas (GWh)', min_value=0, required=True)
	petroleum = forms.IntegerField(label='Petroleum (GWh)', min_value=0, required=True)
	conv_hydro = forms.IntegerField(label='Conv hydro (GWh)', min_value=0, required=True)
	ps_hydro = forms.IntegerField(label='Ps hydro (GWh)', min_value=0, required=True)
	nuclear = forms.IntegerField(label='Nuclear (GWh)', min_value=0, required=True)
	net_imports = forms.IntegerField(label='Net imports (GWh)', min_value=0, required=True)
	other = forms.IntegerField(label='Other (GWh)', min_value=0, required=True)
	waste = forms.IntegerField(label='Waste (GWh)', min_value=0, required=True)
	landfill_gas = forms.IntegerField(label='Landfill gas (GWh)', min_value=0, required=True)
	wood = forms.IntegerField(label='Wood (GWh)', min_value=0, required=True)
	wind = forms.IntegerField(label='Wind (GWh)', min_value=0, required=True)
	solar = forms.IntegerField(label='Solar (GWh)', min_value=0, required=True)
	total = forms.IntegerField(label='Total (GWh)', min_value=0, required=True)

	def save(self, creator):
		electric_data = ElectricData()
		electric_data.city = self.cleaned_data['city']
		electric_data.creator = creator
		electric_data.year = self.cleaned_data['year']
		electric_data.coal = self.cleaned_data['coal']
		electric_data.natural_gas = self.cleaned_data['natural_gas']
		electric_data.petroleum = self.cleaned_data['petroleum']
		electric_data.conv_hydro = self.cleaned_data['conv_hydro']
		electric_data.ps_hydro = self.cleaned_data['ps_hydro']
		electric_data.nuclear = self.cleaned_data['nuclear']
		electric_data.net_imports = self.cleaned_data['net_imports']
		electric_data.other = self.cleaned_data['other']
		electric_data.waste = self.cleaned_data['waste']
		electric_data.landfill_gas = self.cleaned_data['landfill_gas']
		electric_data.wood = self.cleaned_data['wood']
		electric_data.wind = self.cleaned_data['wind']
		electric_data.solar = self.cleaned_data['solar']
		electric_data.total = self.cleaned_data['total']
		electric_data.population = self.cleaned_data['population']
		electric_data.save()
		return electric_data


class CityForm(forms.ModelForm):
	class Meta:
		model = City
		fields = ('name', 'country', 'continent')


class ComparisonForm(forms.Form):
	CHOICES = ((None, '----------'), ('coal', 'Coal'), ('natural_gas', 'Natural gas'),
			   ('petroleum', 'Petroleum'), ('conv_hydro', 'Conv hydro'),
			   ('ps_hydro', 'Ps hydro'), ('nuclear', 'Nuclear'), ('net_imports', 'Net imports'),
			   ('other', 'Other'),
			   ('waste', 'Waste'), ('landfill_gas', 'Landfill gas'), ('wood', 'Wood'), ('wind', 'Wind'),
			   ('solar', 'Solar'),
			   ('total', 'Total'), ('population', 'Population'))

	city = forms.ModelChoiceField(queryset=City.objects.all(), required=True)
	field_1 = forms.ChoiceField(choices=CHOICES, required=True)
	field_2 = forms.ChoiceField(choices=CHOICES, required=False)
