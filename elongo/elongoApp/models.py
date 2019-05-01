from django.db import models


# Create your models here.


class ElectricData(models.Model):
	year = models.IntegerField(blank=False, null=False)
	coal = models.BigIntegerField(blank=False, null=False, default=0)
	natural_gas = models.BigIntegerField(blank=False, null=False, default=0)
	petroleum = models.BigIntegerField(blank=False, null=False, default=0)
	conv_hydro = models.BigIntegerField(blank=False, null=False, default=0)
	ps_hydro = models.BigIntegerField(blank=False, null=False, default=0)
	nuclear = models.BigIntegerField(blank=False, null=False, default=0)
	net_imports = models.BigIntegerField(blank=False, null=False, default=0)
	other = models.BigIntegerField(blank=False, null=False, default=0)
	waste = models.BigIntegerField(blank=False, null=False, default=0)
	landfill_gas = models.BigIntegerField(blank=False, null=False, default=0)
	wood = models.BigIntegerField(blank=False, null=False, default=0)
	wind = models.BigIntegerField(blank=False, null=False, default=0)
	solar = models.BigIntegerField(blank=False, null=False, default=0)
	total = models.BigIntegerField(blank=False, null=False, default=0)

	def __str__(self):
		return self.year
