from rest_framework import serializers
from django.contrib.auth.models import User
from AppAeidl.models import Patient, Medic, Analisi, Study, Entity, Appointment
import django.contrib.auth.password_validation as validators


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

    def create(self, validated_data):
        data = Analisi.objects.create(patient_id=self.initial_data.get("patient"),
                                      medic=self.initial_data.get("medic"),
                                      study_id=self.initial_data.get("study"),
                                      file=validated_data.get("file"))
        return data

    def update(self, instance, validated_data):
        data = Analisi.objects.filter(id=self.data["id"]).update(patient=self.initial_data.get("patient"),
                                      medic=self.data.get("medic")["id"],
                                      study=self.initial_data.get("study"),
                                      file=validated_data.get("file"))
        return data


class EntitySerializers(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = '__all__'


class AppointmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate_password(self, data):
        validators.validate_password(password=data, user=User)
        return data

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.is_active = True
        user.save()
        return user
