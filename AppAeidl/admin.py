from django.contrib import admin
from AppAeidl.models import Medic, Entity, Patient, Study, Role, Exam, Specialty, Person, Company

admin.site.register(Company)
admin.site.register(Person)
admin.site.register(Entity)
admin.site.register(Patient)
admin.site.register(Specialty)
admin.site.register(Role)
admin.site.register(Medic)
admin.site.register(Study)
admin.site.register(Exam)
