from django.urls import path

from .views import CoursesApiView, AvaliationsApiView, CourseApiView, AvaliationApiView

urlpatterns = [
    path("", CoursesApiView.as_view(), name="courses"),
    path("avaliations/", AvaliationsApiView.as_view(), name="avaliations"),
    path("<int:pk>/", CourseApiView.as_view(), name="course"),
    path("avaliations/<int:avaliation_pk>/", AvaliationApiView.as_view(), name="avaliation"),
    path("<int:course_pk>/avaliations/", AvaliationsApiView.as_view(), name="avaliations_by_course"),
    path("<int:course_pk>/avaliations/<int:avaliation_pk>/", AvaliationApiView.as_view(), name="avaliation_by_course"),
]
