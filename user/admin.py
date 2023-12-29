from django.contrib import admin
from .models import Customer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user_info','mobile')

admin.site.register(Customer,CustomerAdmin)
