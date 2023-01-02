from django.shortcuts import render
from django.contrib.auth.models import User
import re



# Create your views here.

def login(request):
	
	user1 = User.objects.filter(email="aazim@travelviacity.com")
	print(user1)
	
	return render(request, 'base/login.html', {'key1':"secret", 'key2':"decrypt"})

def register(request):
	EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
	NO_REGEX = r'(^\+?1?\d{9,15}$)'
	if request.method == "POST":
		uname = request.POST.get('username')

		email = request.POST.get('email')
		if email and not re.match(EMAIL_REGEX, email):
			print("Invalil Email format")
		else:
			print(email)
		number = request.POST.get('number')
		if number and not re.match(NO_REGEX, number):
			print("invalid Number")
		else:
			print(number)
		password = request.POST.get('password')
	
	return render(request, 'base/register.html')

def otp_verification(request):
	if request.method == "POST":
		otpno = request.POST['otp']
		print(otpno)

	return render(request, 'base/verify.html')