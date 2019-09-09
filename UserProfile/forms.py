from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model 
User = get_user_model()
# settings.AUTH_USER_MODEL



g_CHOICES = (('male','male'),('female','female'))

email = forms.EmailField()
gender = forms.ChoiceField(choices=g_CHOICES)

class UserRegisterForm(UserCreationForm):

	class Meta(UserCreationForm):
		model = User
		fields = ['first_name','last_name','email',
		'password1','password2','gender']



from .models import User
from django import forms

class NewForm(forms.ModelForm):
	
	class Meta:
		model = User
		fields = ['first_name','last_name','email','gender',]