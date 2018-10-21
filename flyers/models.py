from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from datetime import date
from sorl.thumbnail import ImageField

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
	city_slug = models.SlugField(max_length=75, blank=True, editable=False)

	def save(self, *args, **kwargs):
		self.city_slug = slugify(self.city)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.city.upper()

	class Meta:
		verbose_name_plural = 'Cities'
		ordering = ['city']


class Store(models.Model):
	city = models.ManyToManyField(City)
	store = models.CharField(max_length=75, unique=True)
	store_slug = models.SlugField(max_length=75, blank=True, editable=False)
	store_logo = models.ImageField(upload_to = 'media/images/stores/')
	store_info = models.TextField(blank=True)

	def save(self, *args, **kwargs):
		self.store_slug = slugify(self.store)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.store.upper()

	class Meta:
		verbose_name_plural = 'Stores'
		ordering = ['store']


class Tag(models.Model):
	tag = models.CharField(max_length=75)
	tag_slug = models.SlugField(max_length=75, blank=True, editable=False)

	def save(self, *args, **kwargs):
		self.tag_slug = slugify(self.tag)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.tag.title()

	class Meta:
		verbose_name_plural = 'Tags'
		ordering = ['tag']


class Category(models.Model):
	cat = models.CharField(max_length=100, verbose_name='Category')
	parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
	cat_slug = models.SlugField(max_length=100, blank=True, editable=False)

	def save(self, *args, **kwargs):
		self.cat = self.cat.title()
		self.cat_slug = slugify(self.cat)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.cat.title()

	class Meta:
		verbose_name_plural = 'Categories'
		ordering = ['cat']


class Coupon(models.Model):
	store = models.ForeignKey(Store, on_delete=models.CASCADE)
	product = models.CharField(max_length=255)
	product_slug = models.SlugField(max_length=255, blank=True, editable=False)
	category = models.ManyToManyField(Category, blank=True)
	price = models.DecimalField(default=0, decimal_places=2, blank=True, max_digits=8)
	sale_price = models.DecimalField(default=0, decimal_places=2, blank=True, max_digits=8)
	product_image = models.ImageField(upload_to = 'media/images/products/')
	product_desc = models.TextField(blank=True)
	tags = models.ManyToManyField(Tag, blank=True)

	def save(self, *args, **kwargs):
		self.product = self.product.title()
		self.product_slug = slugify(self.product)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.product.title()

	class Meta:
		verbose_name_plural = 'Coupons'
		ordering = ['product']


