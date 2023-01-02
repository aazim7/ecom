from django.shortcuts import render
import json
from .cart import TempCart, anonymous, readtempcart
from django.views import View
from .models import Product, ProductImage, Cart, Attribute
from accounts.models import Profile
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt
import uuid
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver

def homepage(request):
	# request.session.flush()
	return render(request, 'base/home.html')

def product_list(request):
	all_products = Product.objects.all()

	return render(request, 'products/shop.html', {'all_products':all_products})

def product_details(request, slug):
	#request.session.flush()
	#readtempcart(request)
	#print(request.session["temp-id"])
	#print(request.session["temp-cart"])
	current_product = Product.objects.filter(slug=slug)
	variations = Attribute.objects.filter(Variation__slug=slug)
	
	for x in current_product:
		related_products = Product.objects.filter(category=x.category).exclude(uid=x.uid)
		#print(related_products)
		return render(request, 'products/single-product-video.html', {'product':x, 'r_products':related_products})

def addcart(request):
	if request.method == "GET":
		dic = request.GET
		p = Product.objects.get(uid=dic['product_id'])
		qt = int(dic['quantity-simple'])
		total_items = 0
		
		if request.user.is_authenticated:
			current_user = request.user
			current_profile = Profile.objects.get(user=current_user)
			
			if request.user.is_superuser:
				print("is super User")
			else:
				#if uuic class is requireds then, uidc = uuid.UUID(dic['product_id'])
				cart=Cart.objects.filter(product__uid=dic['product_id'],customer=current_profile)

				if cart:
					cartInstance=Cart.objects.get(product__uid=dic['product_id'],customer=current_profile)
					# print(cartInstance.total_of_product)
					total = cartInstance.quantity + qt
					cartInstance.quantity = total
					cartInstance.save()
				else:
					addcart=Cart(product=p, customer=current_profile,quantity=qt)
					addcart.save()
				#provide no of items in cart instantly
				related_cart = [p for p in Cart.objects.all() if p.customer==current_profile]
				for qrt in related_cart:
					total_items +=qrt.quantity
					
		else:
			if 'temp-id' not in request.session:
				anonymous(request)
			TempCart(request, args = {dic['product_id']:qt})
			related_cart=readtempcart(request)
			for qs in related_cart:
				total_items +=related_cart[qs]
		da = {
			"cart_quantity" : total_items
		}
		return JsonResponse(da)


#Merging Session and Login Cart 
@receiver(user_logged_in)
def post_save(sender, user, request, **kwargs):
	if 'temp-id' in request.session:
		print("Hello User How are You")
		current_user = request.user
		current_profile = Profile.objects.get(user=current_user)
		gc=readtempcart(request)
		for i in gc:
			cart=Cart.objects.filter(product__uid=i,customer=current_profile)
			if cart:
				try:
					cartInstance=Cart.objects.get(product__uid=i)
					total = cartInstance.quantity + gc[i]
					cartInstance.quantity = total
					cartInstance.save()
				except:
					print("Some Error While Saving, Please Try with Sngle Item")
			else:
				p_ins = Product.objects.get(uid=i)
				addcart=Cart(product=p_ins, customer=current_profile,quantity=gc[i])
				addcart.save()
