from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from Aeidl import settings
from AppAeidl.views import Home, MedicListView, MedicCreateView, MedicUpdateView, MedicDeleteView, PacienteListView, \
    PacienteCreateView, PacienteUpdateView, PacienteDeleteView, ProfileUpdateUser, CompanyDeleteView, CompanyUpdateView, \
    CompanyCreateView, CompanyListView, EntityListView, EntityCreateView, EntityUpdateView, EntityDeleteView

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('medic/', MedicListView.as_view(), name="medic_list"),
    path('medic_create/', MedicCreateView.as_view(), name="medic_create"),
    path('medic_update/<int:pk>/', MedicUpdateView.as_view(), name="medic_update"),
    path('medic_erase/<int:pk>/', MedicDeleteView.as_view(), name="medic_erase"),
    path('patient/', PacienteListView.as_view(), name="paciente_list"),
    path('patient_create/', PacienteCreateView.as_view(), name="paciente_create"),
    path('patient_update/<int:pk>/', PacienteUpdateView.as_view(), name="paciente_update"),
    path('patient_erase/<int:pk>/', PacienteDeleteView.as_view(), name="paciente_erase"),
    path('company/', CompanyListView.as_view(), name="company_list"),
    path('company_create/', CompanyCreateView.as_view(), name="company_create"),
    path('company_update/<int:pk>/', CompanyUpdateView.as_view(), name="company_update"),
    path('company_erase/<int:pk>/', CompanyDeleteView.as_view(), name="company_erase"),
    path('entity/', EntityListView.as_view(), name="entity_list"),
    path('entity_create/', EntityCreateView.as_view(), name="entity_create"),
    path('entity_update/<int:pk>/', EntityUpdateView.as_view(), name="entity_update"),
    path('entity_erase/<int:pk>/', EntityDeleteView.as_view(), name="entity_erase"),
    path('profile/<int:pk>/', ProfileUpdateUser.as_view(), name="profile"),
    path('login/', LoginView.as_view(template_name='Aeidl/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='Aeidl/login.html'), name='logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
