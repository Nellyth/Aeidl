from AppAeidl.models import Patient, Medic, Analisi, Study
from rest_framework import viewsets
from AppAeidl.serializers import PatientSerializers, MedicSerializers, AnalisiSerializers, StudySerializers
from rest_framework.permissions import IsAuthenticated


class PatientView(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializers
    permission_classes = (IsAuthenticated,)


class MedicView(viewsets.ModelViewSet):
    queryset = Medic.objects.all()
    serializer_class = MedicSerializers
    permission_classes = (IsAuthenticated,)


class AnalisiView(viewsets.ModelViewSet):
    queryset = Analisi.objects.all()
    serializer_class = AnalisiSerializers
    permission_classes = (IsAuthenticated,)
