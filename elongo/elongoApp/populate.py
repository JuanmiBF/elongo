import csv
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "elongo.settings")
django.setup()

from elongoApp.models import *


def delete_database_rows():
	if len(ElectricData.objects.all()) != 0:
		ElectricData.objects.all().delete()


def populate():
	with open('electric-generation-by-fuel-type-gwh-beginning-1960.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		city = City.objects.create(name="New York",population= 8000000)
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
												 city = city)
				line_count += 1
		print(f'Processed {line_count} lines.')


delete_database_rows()
populate()
