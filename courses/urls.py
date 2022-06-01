from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (CoursesApiView, 
                    AvaliationsApiView, 
                    CourseApiView, 
                    AvaliationApiView, 
                    CoursesViewSet, 
                    AvaliationsViewSet)


# Padrão Observer
courseRouter = SimpleRouter()
courseRouter.register("courses", CoursesViewSet)
courseRouter.register("avaliations", AvaliationsViewSet)


urlpatterns = [
    path("courses/", CoursesApiView.as_view(), name="courses"),
    path("avaliations/", AvaliationsApiView.as_view(), name="avaliations"),
    path("courses/<int:pk>/", CourseApiView.as_view(), name="course"),
    path("avaliations/<int:avaliation_pk>/", AvaliationApiView.as_view(), name="avaliation"),
    path("courses/<int:course_pk>/avaliations/", AvaliationsApiView.as_view(), name="avaliations_by_course"),
    path("courses/<int:course_pk>/avaliations/<int:avaliation_pk>/", AvaliationApiView.as_view(), name="avaliation_by_course"),
]
