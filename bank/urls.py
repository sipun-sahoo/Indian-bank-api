from django.contrib import admin
from django.urls import path, include
from application import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('bankapi', views.StudentModelViewSet, basename='bank')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify'),
]