import os
from django.conf import settings
from django.db.models import Q
from django.urls import reverse_lazy
from django.http import HttpResponse, Http404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from AppAeidl.models import Medic, Patient, Person, Company, Entity, Specialty, Role, Study, Exam
from AppAeidl.forms import MedicForm, PacienteForm, PersonForm, CompanyForm, EntityForm, SpecialtyForm, RoleForm, \
    StudyForm, ExamForm


class Home(LoginRequiredMixin, TemplateView):
    template_name = 'Aeidl/home.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context["user"] = self.request.user
        return self.render_to_response(context)


class MedicListView(PermissionRequiredMixin, ListView):
    model = Medic
    queryset = Medic.objects.all()
    template_name = 'Aeidl/medic.html'
    permission_required = 'AppAeidl.view_medic'

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return Medic.objects.filter(person=self.request.user)
        return super().get_queryset()


class MedicCreateView(PermissionRequiredMixin, CreateView):
    model = Medic
    form_class = MedicForm
    template_name = 'Aeidl/medic_create.html'
    success_url = reverse_lazy('medic_list')
    permission_required = 'AppAeidl.add_medic'

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return Medic.objects.filter(person=self.request.user)
        return super().get_queryset()


class MedicUpdateView(PermissionRequiredMixin, UpdateView):
    model = Medic
    form_class = MedicForm
    template_name = 'Aeidl/medic_create.html'
    success_url = reverse_lazy('medic_list')
    permission_required = 'AppAeidl.change_medic'

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return Medic.objects.filter(person=self.request.user)
        return super().get_queryset()


class MedicDeleteView(PermissionRequiredMixin, DeleteView):
    model = Medic
    template_name = 'Aeidl/delete.html'
    success_url = reverse_lazy('medic_list')
    permission_required = 'AppAeidl.delete_medic'

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return Medic.objects.filter(person=self.request.user)
        return super().get_queryset()


class PacienteListView(PermissionRequiredMixin, ListView):
    model = Patient
    queryset = Patient.objects.all()
    template_name = 'Aeidl/paciente.html'
    permission_required = 'AppAeidl.view_patient'

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return Patient.objects.filter(person=self.request.user)
        return super().get_queryset()


class PacienteCreateView(PermissionRequiredMixin, CreateView):
    model = Patient
    form_class = PacienteForm
    template_name = 'Aeidl/paciente_create.html'
    success_url = reverse_lazy('paciente_list')
    permission_required = 'AppAeidl.add_patient'

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return Patient.objects.filter(person=self.request.user)
        return super().get_queryset()


class PacienteUpdateView(PermissionRequiredMixin, UpdateView):
    model = Patient
    form_class = PacienteForm
    template_name = 'Aeidl/paciente_create.html'
    success_url = reverse_lazy('paciente_list')
    permission_required = 'AppAeidl.change_patient'

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return Patient.objects.filter(person=self.request.user)
        return super().get_queryset()


class PacienteDeleteView(PermissionRequiredMixin, DeleteView):
    model = Patient
    template_name = 'Aeidl/delete.html'
    success_url = reverse_lazy('paciente_list')
    permission_required = 'AppAeidl.delete_patient'

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return Patient.objects.filter(person=self.request.user)
        return super().get_queryset()


class ProfileUpdateUser(LoginRequiredMixin, UpdateView):
    model = Person
    form_class = PersonForm
    template_name = 'Aeidl/profile.html'
    success_url = reverse_lazy('home')


class CompanyListView(PermissionRequiredMixin, ListView):
    model = Company
    queryset = Company.objects.all()
    template_name = 'Aeidl/company.html'
    permission_required = 'AppAeidl.view_company'


class CompanyCreateView(PermissionRequiredMixin, CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'Aeidl/company_create.html'
    success_url = reverse_lazy('company_list')
    permission_required = 'AppAeidl.add_company'

    def get_queryset(self):
        if not self.request.user.is_superuser:
            try:
                medic = Medic.objects.get(person=self.request.user)
                return Company.objects.filter(Company=medic.company)
            except Medic.DoesNotExist:
                return Company.objects.none()
        return super().get_queryset()


class CompanyUpdateView(PermissionRequiredMixin, UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'Aeidl/company_create.html'
    success_url = reverse_lazy('company_list')
    permission_required = 'AppAeidl.change_company'

    def get_queryset(self):
        if not self.request.user.is_superuser:
            try:
                medic = Medic.objects.get(person=self.request.user)
                return Company.objects.filter(Company=medic.company)
            except Medic.DoesNotExist:
                return Company.objects.none()
        return super().get_queryset()


class CompanyDeleteView(PermissionRequiredMixin, DeleteView):
    model = Company
    template_name = 'Aeidl/delete.html'
    success_url = reverse_lazy('company_list')
    permission_required = 'AppAeidl.delete_company'

    def get_queryset(self):
        if not self.request.user.is_superuser:
            try:
                medic = Medic.objects.get(person=self.request.user)
                return Company.objects.filter(Company=medic.company)
            except Medic.DoesNotExist:
                return Company.objects.none()
        return super().get_queryset()


class EntityListView(PermissionRequiredMixin, ListView):
    model = Entity
    queryset = Entity.objects.all()
    template_name = 'Aeidl/entity.html'
    permission_required = 'AppAeidl.view_entity'


class EntityCreateView(PermissionRequiredMixin, CreateView):
    model = Entity
    form_class = EntityForm
    template_name = 'Aeidl/entity_create.html'
    success_url = reverse_lazy('entity_list')
    permission_required = 'AppAeidl.add_entity'


class EntityUpdateView(PermissionRequiredMixin, UpdateView):
    model = Entity
    form_class = EntityForm
    template_name = 'Aeidl/entity_create.html'
    success_url = reverse_lazy('entity_list')
    permission_required = 'AppAeidl.change_entity'


class EntityDeleteView(PermissionRequiredMixin, DeleteView):
    model = Entity
    template_name = 'Aeidl/delete.html'
    success_url = reverse_lazy('entity_list')
    permission_required = 'AppAeidl.delete_entity'


class SpecialtyListView(PermissionRequiredMixin, ListView):
    model = Specialty
    queryset = Specialty.objects.all()
    template_name = 'Aeidl/specialty.html'
    permission_required = 'AppAeidl.view_specialty'

    def get_queryset(self):
        if not self.request.user.is_superuser:
            try:
                medic = Medic.objects.get(person=self.request.user)
                return Specialty.objects.filter(Company=medic.company)
            except Medic.DoesNotExist:
                return Specialty.objects.none()
        return super().get_queryset()


class SpecialtyCreateView(PermissionRequiredMixin, CreateView):
    model = Specialty
    form_class = SpecialtyForm
    template_name = 'Aeidl/specialty_create.html'
    success_url = reverse_lazy('specialty_list')
    permission_required = 'AppAeidl.add_specialty'

    def get_queryset(self):
        if not self.request.user.is_superuser:
            try:
                medic = Medic.objects.get(person=self.request.user)
                return Specialty.objects.filter(Company=medic.company)
            except Medic.DoesNotExist:
                return Specialty.objects.none()
        return super().get_queryset()


class SpecialtyUpdateView(PermissionRequiredMixin, UpdateView):
    model = Specialty
    form_class = SpecialtyForm
    template_name = 'Aeidl/specialty_create.html'
    success_url = reverse_lazy('specialty_list')
    permission_required = 'AppAeidl.change_specialty'

    def get_queryset(self):
        if not self.request.user.is_superuser:
            try:
                medic = Medic.objects.get(person=self.request.user)
                return Specialty.objects.filter(Company=medic.company)
            except Medic.DoesNotExist:
                return Specialty.objects.none()
        return super().get_queryset()


class SpecialtyDeleteView(PermissionRequiredMixin, DeleteView):
    model = Specialty
    template_name = 'Aeidl/delete.html'
    success_url = reverse_lazy('specialty_list')
    permission_required = 'AppAeidl.delete_specialty'

    def get_queryset(self):
        if not self.request.user.is_superuser:
            try:
                medic = Medic.objects.get(person=self.request.user)
                return Specialty.objects.filter(Company=medic.company)
            except Medic.DoesNotExist:
                return Specialty.objects.none()
        return super().get_queryset()


class RoleListView(PermissionRequiredMixin, ListView):
    model = Role
    queryset = Role.objects.all()
    template_name = 'Aeidl/role.html'
    permission_required = 'AppAeidl.view_specialty'

    def get_queryset(self):
        if not self.request.user.is_superuser:
            try:
                medic = Medic.objects.get(person=self.request.user)
                return Role.objects.filter(Company=medic.company)
            except Medic.DoesNotExist:
                return Role.objects.none()
        return super().get_queryset()


class RoleCreateView(PermissionRequiredMixin, CreateView):
    model = Role
    form_class = RoleForm
    template_name = 'Aeidl/role_create.html'
    success_url = reverse_lazy('role_list')
    permission_required = 'AppAeidl.add_role'

    def get_queryset(self):
        if not self.request.user.is_superuser:
            try:
                medic = Medic.objects.get(person=self.request.user)
                return Role.objects.filter(Company=medic.company)
            except Medic.DoesNotExist:
                return Role.objects.none()
        return super().get_queryset()


class RoleUpdateView(PermissionRequiredMixin, UpdateView):
    model = Role
    form_class = RoleForm
    template_name = 'Aeidl/role_create.html'
    success_url = reverse_lazy('role_list')
    permission_required = 'AppAeidl.change_role'

    def get_queryset(self):
        if not self.request.user.is_superuser:
            try:
                medic = Medic.objects.get(person=self.request.user)
                return Role.objects.filter(Company=medic.company)
            except Medic.DoesNotExist:
                return Role.objects.none()
        return super().get_queryset()


class RoleDeleteView(PermissionRequiredMixin, DeleteView):
    model = Role
    template_name = 'Aeidl/delete.html'
    success_url = reverse_lazy('role_list')
    permission_required = 'AppAeidl.delete_role'

    def get_queryset(self):
        if not self.request.user.is_superuser:
            try:
                medic = Medic.objects.get(person=self.request.user)
                return Role.objects.filter(Company=medic.company)
            except Medic.DoesNotExist:
                return Role.objects.none()
        return super().get_queryset()


class StudyListView(PermissionRequiredMixin, ListView):
    model = Study
    queryset = Study.objects.all()
    template_name = 'Aeidl/study.html'
    permission_required = 'AppAeidl.view_study'

    def get_queryset(self):
        if not self.request.user.is_superuser:
            try:
                medic = Medic.objects.get(person=self.request.user)
                return Study.objects.filter(Company=medic.company)
            except Medic.DoesNotExist:
                return Study.objects.none()
        return super().get_queryset()


class StudyCreateView(PermissionRequiredMixin, CreateView):
    model = Study
    form_class = StudyForm
    template_name = 'Aeidl/study_create.html'
    success_url = reverse_lazy('exam_list')
    permission_required = 'AppAeidl.add_study'

    def get_queryset(self):
        if not self.request.user.is_superuser:
            try:
                medic = Medic.objects.get(person=self.request.user)
                return Study.objects.filter(Company=medic.company)
            except Medic.DoesNotExist:
                return Study.objects.none()
        return super().get_queryset()


class StudyUpdateView(PermissionRequiredMixin, UpdateView):
    model = Study
    form_class = StudyForm
    template_name = 'Aeidl/study_create.html'
    success_url = reverse_lazy('exam_list')
    permission_required = 'AppAeidl.change_study'

    def get_queryset(self):
        if not self.request.user.is_superuser:
            try:
                medic = Medic.objects.get(person=self.request.user)
                return Study.objects.filter(Company=medic.company)
            except Medic.DoesNotExist:
                return Study.objects.none()
        return super().get_queryset()


class StudyDeleteView(PermissionRequiredMixin, DeleteView):
    model = Study
    template_name = 'Aeidl/delete.html'
    success_url = reverse_lazy('exam_list')
    permission_required = 'AppAeidl.delete_study'

    def get_queryset(self):
        if not self.request.user.is_superuser:
            try:
                medic = Medic.objects.get(person=self.request.user)
                return Study.objects.filter(Company=medic.company)
            except Medic.DoesNotExist:
                return Study.objects.none()
        return super().get_queryset()


class ExamListView(PermissionRequiredMixin, ListView):
    model = Exam
    queryset = Exam.objects.all()
    template_name = 'Aeidl/exam.html'
    permission_required = 'AppAeidl.view_exam'

    def get_queryset(self):
        if not self.request.user.is_superuser:
            exam = Exam.objects.filter(Q(medic__person=self.request.user) or Q(patient__person=self.request.user))
            try:
                medic = Medic.objects.get(person=self.request.user)
                return exam.filter(Company=medic.company)
            except Medic.DoesNotExist:
                return exam
        return super().get_queryset()


class ExamCreateView(PermissionRequiredMixin, CreateView):
    model = Exam
    form_class = ExamForm
    template_name = 'Aeidl/exam_create.html'
    success_url = reverse_lazy('exam_list')
    permission_required = 'AppAeidl.add_exam'

    def get_queryset(self):
        if not self.request.user.is_superuser:
            exam = Exam.objects.filter(Q(medic__person=self.request.user) or Q(patient__person=self.request.user))
            try:
                medic = Medic.objects.get(person=self.request.user)
                return exam.filter(Company=medic.company)
            except Medic.DoesNotExist:
                return exam
        return super().get_queryset()


class ExamUpdateView(PermissionRequiredMixin, UpdateView):
    model = Exam
    form_class = ExamForm
    template_name = 'Aeidl/exam_create.html'
    success_url = reverse_lazy('exam_list')
    permission_required = 'AppAeidl.change_exam'

    def get_queryset(self):
        if not self.request.user.is_superuser:
            exam = Exam.objects.filter(Q(medic__person=self.request.user) or Q(patient__person=self.request.user))
            try:
                medic = Medic.objects.get(person=self.request.user)
                return exam.filter(Company=medic.company)
            except Medic.DoesNotExist:
                return exam
        return super().get_queryset()


class ExamDeleteView(PermissionRequiredMixin, DeleteView):
    model = Exam
    template_name = 'Aeidl/delete.html'
    success_url = reverse_lazy('exam_list')
    permission_required = 'AppAeidl.delete_exam'

    def get_queryset(self):
        if not self.request.user.is_superuser:
            exam = Exam.objects.filter(Q(medic__person=self.request.user) or Q(patient__person=self.request.user))
            try:
                medic = Medic.objects.get(person=self.request.user)
                return exam.filter(Company=medic.company)
            except Medic.DoesNotExist:
                return exam
        return super().get_queryset()


def download(request, path):
    if path:
        file_path = os.path.join(settings.MEDIA_ROOT, path.split('media')[1][1:])
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
