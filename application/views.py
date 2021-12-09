from .models import Indianbank
from .serializers import BankSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class StudentModelViewSet(viewsets.ModelViewSet):
  queryset = Indianbank.objects.all()
  serializer_class = BankSerializer
  authentication_classes=[JWTAuthentication]
  permission_classes=[IsAuthenticated]