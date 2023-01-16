from django.db import models
from base.model import BaseModel
from accounts.models import Profile
from django.utils.html import format_html
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class Category(BaseModel):
	category_name = models.CharField(max_length=100)
	slug = models.SlugField(unique= True, null= True, blank= True)
	category_image = models.ImageField(upload_to="categories", null= True, blank= True)

	def __str__(self):
		 return str(self.category_name)

Product_Type = (
	("simple","Simple Product"),
	("variations","With Variations")
	)
class Product(BaseModel):
	product_name = models.CharField(max_length=100)
	ptype = models.CharField(choices=Product_Type,max_length=30)
	quantity = models.IntegerField(null=True)
	slug = models.SlugField(unique =True,  null= True, blank= True)
	category = models.ForeignKey(Category, on_delete= models.CASCADE, related_name="products")
	price = models.IntegerField()
	product_description = models.TextField()
	def __str__(self):
		 return str(self.product_name)


class ProductImage(BaseModel):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_images")
	image = models.ImageField(upload_to="products") 
	
	def imag_n(self):
		 return format_html('<img src="http://127.0.0.1:8000/media/{}" width="140">', self.image)


class AttributeType(BaseModel):
	name=models.CharField(max_length=100, blank=True)
	description=models.TextField(blank=True)
	def __str__(self):
		return str(self.name)

class AttributeValue(BaseModel):
	value=models.CharField(max_length=50, blank=True)
	color_code = models.CharField(max_length=7,blank=True)
	def __str__(self):
		return str(self.value)

class Attribute(BaseModel):
	key=models.ForeignKey(AttributeType, on_delete=models.CASCADE, blank=True, null=True, related_name="atr_key")
	pin=models.ForeignKey(AttributeValue, on_delete=models.CASCADE, blank=True, null=True, related_name="attr_value")
	Variation=models.ForeignKey(Product,on_delete=models.CASCADE, blank=True, null=True, related_name="product_variations")
	def __str__(self):
		return str(self.key)

class Cart(BaseModel):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_cart")
	customer = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
	quantity = models.PositiveIntegerField(default=1)

	@property
	def total_of_product(self):
		total = self.product.price*self.quantity
		return total

# Two ways to define signals
# def email_signal(sender, instance, **kwargs):
# 	print("yes i got signal")
# post_save.connect(email_signal, sender=Category)

# @receiver(pre_save, sender=Category)
# def my_presignal(sender, **kwargs):
# 	print("Befor Email")

# End Two ways to define signals