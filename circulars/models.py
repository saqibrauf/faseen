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


class Flyer(models.Model):
	store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='flyers')
	title = models.CharField(max_length=255)
	date_created = models.DateField(default=date.today, editable=False)
	date_expired = models.DateField(default=date.today)
	slug = models.SlugField(max_length=255, blank=True, editable=False)	
	image = models.ImageField(upload_to='media/images/flyers')
	desc = models.TextField(blank=True)	

	class Meta:
		verbose_name_plural = 'Flyers'
		ordering = ['date_created']	

	def __str__(self):
		return self.title.title()

	def save(self, *args, **kwargs):
		self.title = self.title.title()
		self.slug = slugify(self.title)
		super().save(*args, **kwargs)

class Coupon(models.Model):
	store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='coupons')
	date_created = models.DateField(default=date.today, editable=False)
	date_expired = models.DateField(default=date.today)

	class Meta:
		verbose_name_plural = 'Coupons'
		ordering = ['date_created']	

	def __str__(self):
		return self.product.name.title()

class Product(models.Model):
	flyer = models.ForeignKey(Flyer, on_delete=models.CASCADE, blank=True, null=True, related_name='products')
	coupon = models.OneToOneField(Coupon, on_delete=models.CASCADE, blank=True, null=True, related_name='product')
	name = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255, blank=True, editable=False)
	r_price = models.DecimalField(default=0, decimal_places=2, max_digits=8, verbose_name='Regular Price')
	s_price = models.DecimalField(default=0, decimal_places=2, max_digits=8, verbose_name='Sale Price')
	image = models.ImageField(upload_to='media/images/products')
	desc = models.TextField(blank=True)
	tags = models.ManyToManyField(Tag, blank=True)
	categories = models.ManyToManyField(Category, blank=True)
	
	class Meta:
		verbose_name_plural = 'Products'
		ordering = ['name']	

	def __str__(self):
		return self.name.title()

	def save(self, *args, **kwargs):
		self.name = self.name.title()
		self.slug = slugify(self.name)
		super().save(*args, **kwargs)

