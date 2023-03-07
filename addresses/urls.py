from django.urls import path
from .views import AddressView, AddressDetailView

urlpatterns = [
    path("addresses/", AddressView.as_view()),
    path("addresses/<int:pk>/", AddressDetailView.as_view()),
]
