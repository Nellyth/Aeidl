from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission

from AppAeidl.models import Medic, Entity, Patient, Study, Role, Exam, Specialty, Person, Company


class PersonAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info',
         {'fields': ('identification', 'first_name', 'last_name', 'email', 'gender', 'phone', 'photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('identification', 'username', 'email', 'gender', 'phone', 'password1', 'password2'),
        }),
    )


admin.site.register(Permission)
admin.site.register(Company)
admin.site.register(Person, PersonAdmin)
admin.site.register(Entity)
admin.site.register(Patient)
admin.site.register(Specialty)
admin.site.register(Role)
admin.site.register(Medic)
admin.site.register(Study)
admin.site.register(Exam)
