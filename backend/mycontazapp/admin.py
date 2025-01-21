from django.contrib import admin
from . models import Contact, Category, CustomUser

# Register your models here.
admin.site.register(Contact)
admin.site.register(Category)
admin.site.register(CustomUser)
