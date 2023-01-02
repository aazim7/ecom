from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from django.contrib.auth.models import User, Group
from .userform import Registration, MyLoginForm
from .otpgen import otpgen, otptime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import json
from django.http.response import JsonResponse
from products.cart import readtempcart



def login_page(request):
	
	if not request.user.is_authenticated:
	    form = MyLoginForm()
	    message = ''
	    if request.method == 'POST':
	        form = MyLoginForm(request=request, data=request.POST)
	        if form.is_valid():
	            user = authenticate(
	                username=form.cleaned_data.get('username'),
	                password=form.cleaned_data.get('password')
	            )
	            if user is not None:
	                if user.is_active:
	                	login(request, user)
	                	return redirect("/") 

	            else:
	                message = 'Login failed!'
	                #print(message)
	        else:
	        	message = "Error in Form"
	        	#print("error in form ")
	    return render(request, 'base/login.html', context={'form': form, 'message': message})
	return redirect("/")

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

def register(request):
	#print(request.session['testing'])
	#request.session.flush()

	if request.method == "POST":
		form = Registration(request.POST)
		if form.is_valid():
			messages.success(request, 'Please Verify your Mail!')
			user = form.save()
			group = Group.objects.get(name='Customers')
			user.groups.add(group)
			request.session['otp_asked'] = True
			otp_sign = otpgen()
			request.session['otp'] = otp_sign
			print(otp_sign)
			return redirect('/verification')
	else:
		form = Registration()
		print(form.errors)

	return render(request, 'base/register.html', {'form': form,})

def re_otp(request):
	if request.method == "GET":
		otp_sign = otpgen()
		request.session['otp'] = otp_sign
		response_forXML = {
		'result': "An New Otp Has been Sent to your mail Address"
		};
		print("New OTP - ")
		print(request.session['otp'])
		return JsonResponse(response_forXML)

def otp_verification(request):
	if 'otp_asked' not in request.session:
		return redirect('/')
	else:
		if request.method == "POST":
			otp1 = request.POST['otp1']
			otp2 = request.POST['otp2']
			otp3 = request.POST['otp3']
			otp4 = request.POST['otp4']
			otp_recieved =  otp1+otp2+otp3+otp4

			if otp_recieved == request.session['otp']:
				print("Yes Matched")
				del request.session['otp_asked']

				return redirect('/user-login')
			else:
				print("not matched")
				
			
		return render(request, 'base/verify.html')
