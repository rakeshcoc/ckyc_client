from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required 


# Create your views here.
def index(request):
	pass
#	return render(request,'userprofile/index.html')

def first(request):
	return render(request,'userprofile/first.html')

def js(request):
	if request.method == 'GET':
		return render(request,'onboard/temp.js')

def addform(request):
	if request.method == 'GET':
		return render(request,'onboard/addform.js')

def updateform(request):
	if request.method == 'GET':
		return render(request,'onboard/update.js')
