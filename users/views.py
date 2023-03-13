from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .serializers import UserSerializer, BorrowHistorySerializer
from permissions.isAccountOwnerOrAdmin import IsAccountOwnerOrAdmin
from copies.models import Borrowing


class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrAdmin]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserBorrowHistoryView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = BorrowHistorySerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Borrowing.objects.all()

        return Borrowing.objects.filter(user=self.request.user)