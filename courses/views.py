from rest_framework.generics import  get_object_or_404
from rest_framework import generics

from rest_framework import viewsets

from .models import Course, Avaliation

from .serializers import AvaliationSerializer, CourseSerializer

"""
API V1
"""
class CoursesApiView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class AvaliationsApiView(generics.ListCreateAPIView):
    queryset = Avaliation.objects.all()
    serializer_class = AvaliationSerializer

    def get_queryset(self):
        if self.kwargs.get("course_pk"): #Verifica se foi passado pela url um valor para course_pk
            return self.queryset.filter(course_id=self.kwargs.get("course_pk"))
        return self.queryset.all()

class AvaliationApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliation.objects.all()
    serializer_class = AvaliationSerializer

    def get_object(self):
        
        if self.kwargs.get("course_pk") and self.kwargs.get("avaliation_pk"):
            course_pk = self.kwargs.get("course_pk")
            avaliation_pk = self.kwargs.get("avaliation_pk")
            return get_object_or_404(self.queryset, course_id=course_pk,pk=avaliation_pk)

        return get_object_or_404(self.queryset, pk=self.kwargs.get("avaliation_pk"))

"""
API V2
"""

class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class AvaliationsViewSet(viewsets.ModelViewSet):
    queryset = Avaliation.objects.all()
    serializer_class = AvaliationSerializer