from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import AvaliationSerializer, CourseSerializer

from .models import Course, Avaliation

class CourseApiView(APIView):


    def get(self, request):
        courses = Course.objects.all()
        if courses.count == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)    
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        course = CourseSerializer(data=request.data)
        course.is_valid(raise_exception=True)
        course.save()
        return Response(course.data, status=status.HTTP_201_CREATED)

class AvaliationApiView(APIView):

    def get(self, request):
        avaliations = Avaliation.objects.all()
        if avaliations.count == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AvaliationSerializer(avaliations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        avaliation = AvaliationSerializer(data=request.data)
        avaliation.is_valid(raise_exception=True)
        avaliation.save()
        return Response(avaliation.data, status=status.HTTP_201_CREATED)