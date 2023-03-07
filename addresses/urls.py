from django.urls import path
from .views import AddressView, AdressDetailView

urlpatterns = [
    path("addresses/", AddressView.as_view()),
    path("addresses/<int:pk>/", AdressDetailView.as_view()),
]
