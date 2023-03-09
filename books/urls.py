from django.urls import path

from .views import BookView, BookDetailView, BookFollowingView
urlpatterns = [
    path("books/", BookView.as_view()),
    path("books/<book_id>/", BookDetailView.as_view()),
    path("books/following/<uuid:book_id>/", BookFollowingView.as_view()),
]
