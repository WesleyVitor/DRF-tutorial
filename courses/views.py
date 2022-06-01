from rest_framework.generics import  get_object_or_404
from rest_framework import generics

from rest_framework import viewsets

from rest_framework.decorators import action
from rest_framework.response import Response


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

    """
    O atributo url_path define o nome da url, mas por padrão é o nome do método decorado
    """
    @action(detail=True, methods=['GET'], url_path="avaliations") 
    def avaliations(self, request, pk=None):
        """
        Método já existente pela classe ModelViewSet para pegar uma instância do Modelo da classe(Course)
        """
        course = self.get_object() 
        """
        Serializando para o retorno que eu quero, no caso é avaliations, e passando a instância que quero 
        serializar, no caso as avaliations que estão dentro de course especificado.(Existe dentro do modelo
        avaliation um foreignkey para course, mas foi adicionado um atributo related_name para o course saber
        quais são as suas avaliations)
        """
        serializer = AvaliationSerializer(course.avaliations.all(), many=True)
        return Response(serializer.data)

class AvaliationsViewSet(viewsets.ModelViewSet):
    queryset = Avaliation.objects.all()
    serializer_class = AvaliationSerializer