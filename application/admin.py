
from django.contrib import admin
from .models import Indianbank
# Register your models here.

@admin.register(Indianbank)
class BankAdmin(admin.ModelAdmin):
 list_display = ['id', 'bankname', 'accno', 'ifsccode']