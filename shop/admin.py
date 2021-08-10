from django.contrib import admin

# Register your models here.
from .models import produts,contact_user

admin.site.register(produts)
admin.site.register(contact_user)
