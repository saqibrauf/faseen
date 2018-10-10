from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

class Country(models.Model):
	country = models.CharField(max_length=75, unique=True)
	country_slug = models.SlugField(max_length=75, blank=True, editable=False)

	def save(self, *args, **kwargs):
		self.country_slug = slugify(self.country)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.country.upper()

	class Meta:
		verbose_name_plural = 'Countries'
		ordering = ['country']


class City(models.Model):
	country = models.ForeignKey(Country, on_delete=models.CASCADE)
	city = models.CharField(max_length=75)
	city_code = models.CharField(max_length=75, unique=True)
	city_slug = models.SlugField(max_length=75, blank=True, editable=False)

	def save(self, *args, **kwargs):
		self.city_slug = slugify(self.city)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.city.upper()

	class Meta:
		verbose_name_plural = 'Cities'
		ordering = ['city']



class Area(models.Model):
	city = models.ForeignKey(City, on_delete=models.CASCADE)
	area = models.CharField(max_length=75, unique=True)
	area_slug = models.SlugField(max_length=75, blank=True, editable=False)

	def save(self, *args, **kwargs):
		self.area_slug = slugify(self.area)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.area.upper()

	class Meta:
		verbose_name_plural = 'Areas'
		ordering = ['area']