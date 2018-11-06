from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from datetime import date
from sorl.thumbnail import ImageField
from mptt.models import MPTTModel, TreeForeignKey

class Location(MPTTModel):
	name = models.CharField(max_length=70, unique=True)
	parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

	class MPTTMeta:
		order_insertion_by = ['name']

	class Meta:
		verbose_name_plural = 'Locations'
		ordering = ['name']

	def __str__(self):
		return self.name.upper()


class Store(models.Model):
	location = models.ManyToManyField(Location)
	name = models.CharField(max_length=150, unique=True)
	slug = models.SlugField(max_length=150, blank=True, editable=False)
	logo = models.ImageField(upload_to = 'media/images/stores/')
	desc = models.TextField(blank=True)

	class Meta:
		verbose_name_plural = 'Stores'
		ordering = ['name']

	def __str__(self):
		return self.name.upper()

	def save(self, *args, **kwargs):
		self.name = self.name.title()
		self.slug = slugify(self.name)
		super().save(*args, **kwargs)


class Tag(models.Model):
	tag = models.CharField(max_length=75)
	slug = models.SlugField(max_length=75, blank=True, editable=False)

	class Meta:
		verbose_name_plural = 'Tags'
		ordering = ['tag']	

	def __str__(self):
		return self.tag.title()

	def save(self, *args, **kwargs):
		self.tag = self.tag.title()
		self.slug = slugify(self.tag)
		super().save(*args, **kwargs)


class Category(MPTTModel):
	name = models.CharField(max_length=70, unique=True)
	parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

	class MPTTMeta:
		order_insertion_by = ['name']

	class Meta:
		verbose_name_plural = 'Categories'
		ordering = ['name']

	def __str__(self):
		return self.name.upper()


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

	class Meta:
		verbose_name_plural = 'Coupons'
		ordering = ['product']	

	def __str__(self):
		return self.product.title()

	def save(self, *args, **kwargs):
		self.product = self.product.title()
		self.product_slug = slugify(self.product)
		super().save(*args, **kwargs)

	


