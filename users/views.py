from .models import CustomUser
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from .serializers import CustomTokenObtainPairSerializer, CustomUserSeralizer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSeralizer
    rendere_classes = [JSONRenderer]


    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            return[IsAuthenticated()]
        return []



from rest_framework_simplejwt.views import TokenObtainPairView

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer