import csv
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "elongo.settings")
django.setup()

from elongoApp.models import *


def delete_database_rows():
	if len(City.objects.all()) != 0:
		City.objects.all().delete()
	if len(ElectricData.objects.all()) != 0:
		ElectricData.objects.all().delete()

def create_population_dict():
	population = dict()
	population['1960'] = 7781984
	population['1961'] = 7791984
	population['1962'] = 7798198
	population['1963'] = 7801424
	population['1964'] = 7822924
	population['1965'] = 7829318
	population['1966'] = 7835947
	population['1967'] = 7848925
	population['1968'] = 7851654
	population['1969'] = 7872814
	population['1970'] = 7895563
	population['1971'] = 7881115
	population['1972'] = 7869654
	population['1973'] = 7866815
	population['1974'] = 7845759
	population['1975'] = 7836924
	population['1976'] = 7620322
	population['1977'] = 7428841
	population['1978'] = 7395954
	population['1979'] = 7158361
	population['1980'] = 7071639
	population['1981'] = 7082895
	population['1982'] = 7085645
	population['1983'] = 7102215
	population['1984'] = 7103842
	population['1985'] = 7109624
	population['1986'] = 7116328
	population['1987'] = 7195784
	population['1988'] = 7243485
	population['1989'] = 7285991
	population['1990'] = 7322671
	population['1991'] = 7389458
	population['1992'] = 7428215
	population['1993'] = 7498659
	population['1994'] = 7526842
	population['1995'] = 7587332
	population['1996'] = 7695884
	population['1997'] = 7752515
	population['1998'] = 7843624
	population['1999'] = 7995845
	population['2000'] = 8008547
	population['2001'] = 8001461
	population['2002'] = 8015547
	population['2003'] = 8095884
	population['2004'] = 8089216
	population['2005'] = 8114349
	population['2006'] = 8112281
	population['2007'] = 8156964
	population['2008'] = 8148774
	population['2009'] = 8176518
	population['2010'] = 8193703
	population['2011'] = 8292688
	population['2012'] = 8383504
	population['2013'] = 8458642
	population['2014'] = 8521135
	population['2015'] = 8582459

	return population


def populate():
	population = create_population_dict()
	with open('electric-generation-by-fuel-type-gwh-beginning-1960.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		city = City.objects.create(name="New York",country="USA",continent="America")
		if not User.objects.filter(username='admin').first():
			User.objects.create_superuser('admin', '', 'patata123')
		superuser = User.objects.filter(username='admin').first()
		for row in csv_reader:
			if line_count == 0:
				print(f'Column names are {", ".join(row)}')
				line_count += 1
			else:
				print('{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format(row[0], row[1], row[2], row[3],
																						  row[4], row[5], row[6], row[7],
																						  row[8], row[9], row[10], row[11],
																						  row[12], row[13], row[14]))

				ElectricData.objects.create(year=row[0] if row[0] != '' else 0, coal=row[1] if row[1] != '' else 0,
												 natural_gas=row[2] if row[2] != '' else 0,
												 petroleum=row[3] if row[3] != '' else 0,
												 conv_hydro=row[4] if row[4] != '' else 0,
												 ps_hydro=row[5] if row[5] != '' else 0,
												 nuclear=row[6] if row[6] != '' else 0,
												 net_imports=row[7] if row[7] != '' else 0,
												 other=row[8] if row[8] != '' else 0, waste=row[9] if row[9] != '' else 0,
												 landfill_gas=row[10] if row[10] != '' else 0,
												 wood=row[11] if row[11] != '' else 0, wind=row[12] if row[12] != '' else 0,
												 solar=row[13] if row[13] != '' else 0,
												 total=row[14] if row[14] != '' else 0,
												 city = city, population= population[str(row[0])], creator=superuser)
				line_count += 1
		print(f'Processed {line_count} lines.')


delete_database_rows()
populate()
