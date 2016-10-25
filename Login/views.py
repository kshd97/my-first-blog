from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User,UserManager,AbstractBaseUser
from django.contrib.auth import authenticate,login,logout
from .models import UserProfile

# Create your views here.
def index(request):
	return render(request,'Login/signin.html',None)

def signin(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		print(user)
		if user is None:
			return render(request,'Login/signin.html',{'error':'Invalid username or password'})
		else:
			login(request,user)
		return redirect('/Game')#render the dashboard page
	else:
		return render(request,'Login/signin.html',None)

def signup(request):
# print "hi there"
# if request.user.is_authenticated() == True and request.user.is_active == True:
# 	return render(request,'Login/dashboard.html',None)
	print("hi")
	if request.method == 'POST':
		print(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		password2 = request.POST['re_password']
		firstName = request.POST['first_name']
		lastName = request.POST['last_name']
		if password2 != password:
			return render(request,'Login/signup.html',{'error':'Password doesn\'t match'})
		emailAddr = request.POST['email']
		contact = request.POST.get('contact')
		address = request.POST['address']
		# regno = request.POST.get('regno')
		try:
			u = User._default_manager.get(username__iexact=username) #fix for case sensitive username
			return render(request,'Login/signup.html',{'error':'username already already exists!'})
		except User.DoesNotExist:
			user = User.objects.create_user(username=username,email=emailAddr,first_name=firstName,last_name=lastName)
			user.set_password(password)
			user.is_active = True
			# print "hi there"
			user.save()
			profileobject = UserProfile(user=user,address=address,mbno=contact)
			profileobject.save()
			print("HELLOO")
			print (profileobject)
			print("HELLOO")
			user.backend = 'django.contrib.auth.backends.ModelBackend' #user backend error fix
			authenticate(username=username,password=password)
			login(request,user)
			return redirect('/Game')
	else:
		return render(request,'Login/signup.html',None) 

def signout(request):
	logout(request)
	return render(request,'Login/signin.html',None)
def lksignup(request):
	return render(request,'Login/signup.html',None)