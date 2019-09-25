from rest_framework import serializers

from AppAeidl.models import Patient, Medic, Analisi, Study


class PatientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = \
            (
                'id',
                'identificacion',
                'name',
                'genero',
                'fecha_nac',
                'ocupacion',
                'telefono',
                'direccion',
                'entity'
            )


class MedicSerializers(serializers.ModelSerializer):
    class Meta:
        model = Medic
        fields = \
            (
                'id',
                'identificacion',
                'name',
                'user',
                'telefono',
                'genero',
                'appointment'
            )


class StudySerializers(serializers.ModelSerializer):
    class Meta:
        model = Study
        fields = '__all__'


class AnalisiSerializers(serializers.ModelSerializer):
    medic = MedicSerializers(read_only=True)
    patient = PatientSerializers(read_only=True)
    study = StudySerializers(read_only=True)

    class Meta:
        model = Analisi
        fields = \
            (
                'id',
                'patient',
                'medic',
                'study',
                'fecha',
                'file'
            )
