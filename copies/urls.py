from django.urls import path
from .views import CopyView, CopyDetailView, CopyListView


urlpatterns = [
    path("copies/<book_id>/", CopyView.as_view()),
    path("copies/", CopyListView.as_view()),
    path("copies/<book_id>/", CopyDetailView.as_view()),
]
