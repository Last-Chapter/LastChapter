from django.urls import path
from .views import CopyView, CopyDetailView

urlpatterns = [
    path("copies/", CopyView.as_view()),
    path("copies/<pk>/", CopyDetailView.as_view()),
]
