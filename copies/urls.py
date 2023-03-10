from django.urls import path
from .views import (
    CopyView,
    CopyDetailView,
    CopyListView,
    CopyBorrowingView,
    ReturnBorrowingView,
)

urlpatterns = [
    path("copies/<uuid:book_id>/", CopyView.as_view()),
    path("copies/", CopyListView.as_view()),
    path("copy/<uuid:copy_id>/", CopyDetailView.as_view()),
    path("copy/borrowing/<uuid:copy_id>/", CopyBorrowingView.as_view()),
    path("copy/borrowing/return/<uuid:copy_id>/", ReturnBorrowingView.as_view()),
]
