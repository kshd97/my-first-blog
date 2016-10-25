from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User,UserManager,AbstractBaseUser
from django.contrib.auth import authenticate,login,logout
from Login.models import UserProfile
from .models import GroupDetails

# Create your views here.
def index(request):
	user = request.user
	print("HELLO")
	print(user)
	print("HELLO")
	u = UserProfile.objects.filter(user = user)
	if len(u) > 0:
		if u[0].grpid is None: 
			return render(request,'Game/sportform.html')
		else:
			groups = GroupDetails.objects.filter(grpid = u[0].grpid.grpid)
			users = UserProfile.objects.filter(grpid = u[0].grpid.grpid)
			print("HELOO")
			print(groups)
			print("HELOO")
			for k in groups:
				k.save()
			return render(request,'Game/group.html',{'groups':k,'users':users})
	else:
		raise Http404
#done
def sportform(request):
	if  request.method == 'POST':
		sport = request.POST['Sport']
		city = request.POST['City']
		location = request.POST['Location']
		starttime = request.POST['StartTime']
		endtime = request.POST['EndTime']
		q=GroupDetails.objects.filter(Sport=sport)
		q=GroupDetails.objects.filter(City=city)
		# q=GroupDetails.objects.filter(StartTime <= starttime)
		# q=GroupDetails.objects.filter(EndTime >= starttime)
		print("Reached form")
		return render(request,'Game/list.html',{'groups':q,'sport':sport,'city':city,'location':location,'starttime':starttime,'endtime':endtime})
	else:
		raise Http404

def creategroup(request):
	if  request.method == 'POST':
		sport = request.POST['sport']
		city = request.POST['city']
		location = request.POST['location']
		starttime = request.POST['starttime']
		endtime= request.POST['endtime']
		groupobject = GroupDetails(Sport=sport,City=city,Location=location,StartTime=starttime,EndTime=endtime)
		groupobject.save()
		# q=GroupDetails.objects.filter(Sport=sport)
		# q=GroupDetails.objects.filter(City=city)
		# q=GroupDetails.objects.filter(StartTime <= starttime)
		# q=GroupDetails.objects.filter(Endtime >= starttime)
		print("HELOO")
		u = request.user
		print(u)
		print("HELLO")
		us = UserProfile.objects.filter(user = u).update(grpid=groupobject.grpid)
		#for k in us:
			#k.grpid=groupobject.grpid
		return render(request,'Game/group.html',{'groups':groupobject})
	else:
		raise Http404

def update(request):
	print("chal jaa")
	us = request.user
	print(us)	
	grpid = request.GET.get('gi')
	u = UserProfile.objects.filter(user = us).update(grpid=grpid)
	#for k in u:
		#k.grpid=grpid
	return redirect('/Game')

# def list(request):
# 	user = request.user
# 	gi = request.GET.get('gi')
# 	grp = GroupDetails.objects.filter(grpid=gi)
# 	u = UserProfile.objects.filter(grpid = gi)



