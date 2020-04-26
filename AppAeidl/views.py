from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView

from AppAeidl.forms import MedicForm, PacienteForm, PersonForm, CompanyForm, EntityForm
from AppAeidl.models import Medic, Patient, Person, Company, Entity


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


class MedicCreateView(PermissionRequiredMixin, CreateView):
    model = Medic
    form_class = MedicForm
    template_name = 'Aeidl/medic_create.html'
    success_url = reverse_lazy('medic_list')
    permission_required = 'AppAeidl.add_medic'


class MedicUpdateView(PermissionRequiredMixin, UpdateView):
    model = Medic
    form_class = MedicForm
    template_name = 'Aeidl/medic_create.html'
    success_url = reverse_lazy('medic_list')
    permission_required = 'AppAeidl.change_medic'


class MedicDeleteView(PermissionRequiredMixin, DeleteView):
    model = Medic
    template_name = 'Aeidl/delete.html'
    success_url = reverse_lazy('medic_list')
    permission_required = 'AppAeidl.delete_medic'


class PacienteListView(PermissionRequiredMixin, ListView):
    model = Patient
    queryset = Patient.objects.all()
    template_name = 'Aeidl/paciente.html'
    permission_required = 'AppAeidl.view_patient'


class PacienteCreateView(PermissionRequiredMixin, CreateView):
    model = Patient
    form_class = PacienteForm
    template_name = 'Aeidl/paciente_create.html'
    success_url = reverse_lazy('paciente_list')
    permission_required = 'AppAeidl.add_patient'


class PacienteUpdateView(PermissionRequiredMixin, UpdateView):
    model = Patient
    form_class = PacienteForm
    template_name = 'Aeidl/paciente_create.html'
    success_url = reverse_lazy('paciente_list')
    permission_required = 'AppAeidl.change_patient'


class PacienteDeleteView(PermissionRequiredMixin, DeleteView):
    model = Patient
    template_name = 'Aeidl/delete.html'
    success_url = reverse_lazy('paciente_list')
    permission_required = 'AppAeidl.delete_patient'


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


class CompanyUpdateView(PermissionRequiredMixin, UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'Aeidl/company_create.html'
    success_url = reverse_lazy('company_list')
    permission_required = 'AppAeidl.change_company'


class CompanyDeleteView(PermissionRequiredMixin, DeleteView):
    model = Company
    template_name = 'Aeidl/delete.html'
    success_url = reverse_lazy('company_list')
    permission_required = 'AppAeidl.delete_company'


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
