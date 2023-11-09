from django.contrib import admin
from .models import Client, Contact, Contract, Project

# Register your models here.
admin.site.register(Client)
admin.site.register(Contact)
admin.site.register(Contract)
admin.site.register(Project)