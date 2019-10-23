import mimetypes
import os
from django.http import HttpResponse, Http404
from AppAeidl.models import Patient, Medic, Analisi, Entity, Appointment, Study
from rest_framework import viewsets, mixins, status
from AppAeidl.serializers import PatientSerializers, MedicSerializers, AnalisiSerializers, EntitySerializers, \
    AppointmentSerializers, UserSerializers, StudySerializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class PatientView(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializers
    permission_classes = (IsAuthenticated,)


class MedicView(viewsets.ModelViewSet):
    queryset = Medic.objects.all()
    serializer_class = MedicSerializers
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        user_serializers = UserSerializers(data={
            'username': request.data.get('user'),
            'password': request.data.get('password'),
            'email': request.data.get('email')})
        user_serializers.is_valid(raise_exception=True)
        user = user_serializers.save()
        data = request.data.copy()
        data['user'] = user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response("Successful Registration", status=status.HTTP_201_CREATED, headers=headers)


class AnalisisView(viewsets.ModelViewSet):
    queryset = Analisi.objects.all()
    serializer_class = AnalisiSerializers
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data["medic"] = self.request.user
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class EntityView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializers


class AppointmentView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializers


class StudyView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Study.objects.all()
    serializer_class = StudySerializers


def download_file(request):
    try:
        file = Analisi.objects.get(pk=request.GET.get('pk')).file
        type, encoding = mimetypes.guess_type(file.name)
        if type is None:
            type = 'application/octet-stream'
        response = HttpResponse(file.read(), content_type=type)
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file.name)
        return response
    except Exception as e:
        raise Http404(e)
