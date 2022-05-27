from django.urls import path

from .views import CourseApiView, AvaliationApiView

urlpatterns = [
    path("", CourseApiView.as_view(), name="courses"),
    path("avaliations/", AvaliationApiView.as_view(), name="avaliations"),
]
