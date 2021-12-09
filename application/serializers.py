from rest_framework import serializers
from .models import Indianbank

class BankSerializer(serializers.ModelSerializer):
 class Meta:
  model = Indianbank
  fields = ['id', 'bankname', 'accno', 'ifsccode']