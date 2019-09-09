from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager

CHOICES = (('RF','RF'),('RA','RA'),('M.Tech','M.Tech'))
g_CHOICES = (('male','male'),('female','female'))

class User(AbstractUser):
	username = None
	email = models.EmailField(unique=True)
	gender = models.CharField(choices=g_CHOICES,max_length=60)
	is_checker = models.BooleanField(default=False)
	is_maker = models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = CustomUserManager()

	def __str__(self):
	    return self.email

	class Meta:
	    verbose_name = _('user')
	    verbose_name_plural = _('users')

	def get_full_name(self):
	    full_name = '%s %s' % (self.first_name, self.last_name)
	    return full_name.strip()

	def get_short_name(self):
	    return self.first_name

	def get_absolute_url(self):
		return reverse('userdetail',kwargs={"id":self.id})




