from .models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserRegisterForm

class CustomUserAdmin(UserAdmin):
    add_form = UserRegisterForm
#    form = CustomUserChangeForm
    model = User
    list_display = ('email','is_maker','is_checker')
    list_filter = ('email', 'is_maker','is_checker',)
    fieldsets = (
        (None, {'fields': ('email', 'password','gender','is_maker','is_checker',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','gender','password1', 'password2',
            		   'is_maker','is_checker','is_staff','is_active',)}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, CustomUserAdmin)