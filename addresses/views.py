from .models import Address
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import AddressSerializer
from permissions.isAccountOwnerOrAdmin import IsAccountOwnerOrAdmin


class AddressView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrAdmin]
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrAdmin]

    queryset = Address.objects.all()
    serializer_class = AddressSerializer
