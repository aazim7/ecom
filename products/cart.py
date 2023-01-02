# from .models import Product, ProductImage, Cart
# import collections  




def anonymous(request):
	temp_id = request.session["temp-id"] = "7890uehz2jhb87yjbh"
	request.session["temp-cart"] = []

def TempCart(request, args ):
	product_list = request.session["temp-cart"]
	
	product_list.append(args)
	
	request.session["temp-cart"] = product_list
	
	print("Cart --")
	#print(request.session["temp-cart"])
	return(product_list)

def readtempcart(request):
	all_temp_cart = request.session["temp-cart"]
	
	final_cart = {}
	for x in all_temp_cart:
		for k in x.keys():
			final_cart[k] = final_cart.get(k, 0) + x[k]
	print(final_cart)
	return(final_cart)
	
		


			
