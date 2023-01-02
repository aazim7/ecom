# Custom Context Processor
from .models import Cart
from accounts.models import Profile
from django.contrib.auth.models import User
from .cart import TempCart, anonymous, readtempcart


def cart_qty(request):
	print("context processor")
	if request.user.is_authenticated:
		current_user = request.user
		current_profile = Profile.objects.get(user=current_user)
		related_cart = [p for p in Cart.objects.all() if p.customer==current_profile]
		number_of_items=0
		if related_cart:
			for x in related_cart:
				number_of_items += x.quantity
			
			return{
				'items_no':number_of_items,
			}
		else:
			return{
				'items_no':False,
			}
	else:
		if 'temp-id' in request.session:
			number_of_items=0
			related_cart=readtempcart(request)
			for qs in related_cart:
				number_of_items +=related_cart[qs]
			return{
				'items_no':number_of_items,
			}
		else:
			return {
				'items_no':False,
			}
