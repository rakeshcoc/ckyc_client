# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from .forms import UserRegisterForm,NewForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect


def login_success(request):
	if request.user.is_maker:
		val=request.user
		return redirect('/')

	elif request.user.is_checker:
		val=request.user
		return HttpResponse('hi checker'+str(val))
	else:
		return HttpResponse('you are authenticated')


def index(request):
	return render(request,'index.html')

def maker_register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_maker = True
			user.save()
			# username = form.cleaned_data.get('username')
			# form.cleaned_data.get('username')
			return HttpResponse('thnaks')


	else:
		form = UserRegisterForm()
	return render(request,'registration/register.html',{'form':form})


def checker_register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_checker = True
			user.save()
			# username = form.cleaned_data.get('username')
			# form.cleaned_data.get('username')
			return HttpResponse('thnaks')
	else:
		form = UserRegisterForm()
	return render(request,'registration/register.html',{'form':form})

def register(request):
	pass
# 	if request.method == 'POST':
# 		form = UserRegisterForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			username = form.cleaned_data.get('username')
# 			messages.success(request,('Account created for '+str(username)))
# 			return redirect('/')
# 	else:
# 		form = UserRegisterForm()
# 	return render(request,'registar/register.html',{'form':form})


@login_required
def user_detail(request,username=None):
	#instance=OrgList.objects.get(id=id)
	instance = get_object_or_404(User,username=username)
	context ={
			'instance' : instance,

	}
	return  render (request,"users/profile.html" , context)



@login_required
def user_update(request,username=None):
	
	username1=request.user.username
	if username !=username1:
		return HttpResponseRedirect('/myprofile/'+str(username1)+'/edit')

	instance = get_object_or_404(User,username=username)
	form = NewForm(request.POST or None,request.FILES or None ,instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())

	context ={
			  'instance' : instance,
			  'form':form ,
	}
	return  render (request,"users/edit.html" , context)

#@login_required
def logged_in_view(request):
	if request.user.is_authenticated:
		HttpResponseRedirect("/chat/")
	else:
		HttpResponseRedirect("/login/")

from django.contrib.auth.views import LoginView

def custom_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/chat/')
    else:
        return LoginView(request)




def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {
        'form': form
    })

def user_settings(request):
	return render(request,'users/settings.html')







