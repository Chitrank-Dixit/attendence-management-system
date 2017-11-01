from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from attendence.models import Student, Attendence
from attendence.serializers import StudentSerializer, AttendenceSerializer
from miscellaneous.utils import CustomMetaDataMixin
from braces.views import CsrfExemptMixin
from attendence.permissions import IsTeacher

class StudentViewSet(CustomMetaDataMixin, CsrfExemptMixin, viewsets.ModelViewSet):
    """

    """
    authentication_classes = [SessionAuthentication, ]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (permissions.IsAuthenticated, IsTeacher)


class AttendenceViewSet(CustomMetaDataMixin, CsrfExemptMixin, viewsets.ModelViewSet):
    """

    """
    authentication_classes = [SessionAuthentication, ]
    permission_classes = [permissions.IsAuthenticated, IsTeacher]
    queryset = Attendence.objects.all()
    serializer_class = AttendenceSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({"data": "Attendence has been recorded"})

    # pass a parameter student_id
    @list_route(methods=['get'], serializer_class=AttendenceSerializer, url_path='get-student-attendence')
    def get_student_attendence(self, request):
        student_id = self.request.query_params.get('student_id')
        queryset = Attendence.objects.filter(student_id=student_id)
        serialized_data = self.get_serializer(queryset, many=True).data
        return Response(serialized_data)





