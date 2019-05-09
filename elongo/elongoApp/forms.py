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
			   ('total', 'Total'))

	city = forms.ModelChoiceField(queryset=City.objects.all(), required=True)
	field_1 = forms.ChoiceField(choices=CHOICES, required=True)
	field_2 = forms.ChoiceField(choices=CHOICES, required=False)

class PieChartForm(forms.Form):
	CHOICES = (('1920', '1920'),
			   ('1921', '1921'),
			   ('1922', '1922'),
			   ('1923', '1923'),
			   ('1924', '1924'),
			   ('1925', '1925'),
			   ('1926', '1926'),
			   ('1927', '1927'),
			   ('1928', '1928'),
			   ('1929', '1929'),
			   ('1930', '1930'),
			   ('1931', '1931'),
			   ('1932', '1932'),
			   ('1933', '1933'),
			   ('1934', '1934'),
			   ('1935', '1935'),
			   ('1936', '1936'),
			   ('1937', '1937'),
			   ('1938', '1938'),
			   ('1939', '1939'),
			   ('1940', '1940'),
			   ('1941', '1941'),
			   ('1942', '1942'),
			   ('1943', '1943'),
			   ('1944', '1944'),
			   ('1945', '1945'),
			   ('1946', '1946'),
			   ('1947', '1947'),
			   ('1948', '1948'),
			   ('1949', '1949'),
			   ('1950', '1950'),
			   ('1951', '1951'),
			   ('1952', '1952'),
			   ('1953', '1953'),
			   ('1954', '1954'),
			   ('1955', '1955'),
			   ('1956', '1956'),
			   ('1957', '1957'),
			   ('1958', '1958'),
			   ('1959', '1959'),
			   ('1960', '1960'),
			   ('1961', '1961'),
			   ('1962', '1962'),
			   ('1963', '1963'),
			   ('1964', '1964'),
			   ('1965', '1965'),
			   ('1966', '1966'),
			   ('1967', '1967'),
			   ('1968', '1968'),
			   ('1969', '1969'),
			   ('1970', '1970'),
			   ('1971', '1971'),
			   ('1972', '1972'),
			   ('1973', '1973'),
			   ('1974', '1974'),
			   ('1975', '1975'),
			   ('1976', '1976'),
			   ('1977', '1977'),
			   ('1978', '1978'),
			   ('1979', '1979'),
			   ('1980', '1980'),
			   ('1981', '1981'),
			   ('1982', '1982'),
			   ('1983', '1983'),
			   ('1984', '1984'),
			   ('1985', '1985'),
			   ('1986', '1986'),
			   ('1987', '1987'),
			   ('1988', '1988'),
			   ('1989', '1989'),
			   ('1990', '1990'),
			   ('1991', '1991'),
			   ('1992', '1992'),
			   ('1993', '1993'),
			   ('1994', '1994'),
			   ('1995', '1995'),
			   ('1996', '1996'),
			   ('1997', '1997'),
			   ('1998', '1998'),
			   ('1999', '1999'),
			   ('2000', '2000'),
			   ('2001', '2001'),
			   ('2002', '2002'),
			   ('2003', '2003'),
			   ('2004', '2004'),
			   ('2005', '2005'),
			   ('2006', '2006'),
			   ('2007', '2007'),
			   ('2008', '2008'),
			   ('2009', '2009'),
			   ('2010', '2010'),
			   ('2011', '2011'),
			   ('2012', '2012'),
			   ('2013', '2013'),
			   ('2014', '2014'),
			   ('2015', '2015'),
			   ('2016', '2016'),
			   ('2017', '2017'),
			   ('2018', '2018'),
			   ('2019', '2019'))

	city = forms.ModelChoiceField(queryset=City.objects.all(), required=True)
	year = forms.ChoiceField(choices=CHOICES, required=True)
