from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import SimpleRouter
from django.shortcuts import render
from .views import *
from django.urls import path, include

router = SimpleRouter()
router.register(r'api', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', CustomTokenObtainPairView.as_view(), name="token"),
    path('token/refresh/', TokenRefreshView.as_view(), name="refresh")
]
