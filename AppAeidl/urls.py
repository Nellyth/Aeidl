from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from Aeidl import settings
from AppAeidl.views import Home, MedicListView, MedicCreateView, MedicUpdateView, MedicDeleteView, PacienteListView, \
    PacienteCreateView, PacienteUpdateView, PacienteDeleteView, ProfileUpdateUser, CompanyDeleteView, CompanyUpdateView, \
    CompanyCreateView, CompanyListView, EntityListView, EntityCreateView, EntityUpdateView, EntityDeleteView, \
    SpecialtyListView, SpecialtyCreateView, SpecialtyUpdateView, SpecialtyDeleteView, RoleListView, RoleCreateView, \
    RoleUpdateView, RoleDeleteView, StudyDeleteView, StudyUpdateView, StudyCreateView, StudyListView, ExamListView, \
    ExamCreateView, ExamUpdateView, ExamDeleteView

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
    path('specialty/',  SpecialtyListView.as_view(), name="specialty_list"),
    path('specialty_create/',  SpecialtyCreateView.as_view(), name="specialty_create"),
    path('specialty_update/<int:pk>/',  SpecialtyUpdateView.as_view(), name="specialty_update"),
    path('specialty_erase/<int:pk>/',  SpecialtyDeleteView.as_view(), name="specialty_erase"),
    path('role/',  RoleListView.as_view(), name="role_list"),
    path('role_create/',  RoleCreateView.as_view(), name="role_create"),
    path('role_update/<int:pk>/',  RoleUpdateView.as_view(), name="role_update"),
    path('role_erase/<int:pk>/',  RoleDeleteView.as_view(), name="role_erase"),
    path('study/',  StudyListView.as_view(), name="study_list"),
    path('study_create/',  StudyCreateView.as_view(), name="study_create"),
    path('study_update/<int:pk>/',  StudyUpdateView.as_view(), name="study_update"),
    path('study_erase/<int:pk>/',  StudyDeleteView.as_view(), name="study_erase"),
    path('exam/', ExamListView.as_view(), name="exam_list"),
    path('exam_create/', ExamCreateView.as_view(), name="exam_create"),
    path('exam_update/<int:pk>/', ExamUpdateView.as_view(), name="exam_update"),
    path('exam_erase/<int:pk>/', ExamDeleteView.as_view(), name="exam_erase"),
    path('profile/<int:pk>/', ProfileUpdateUser.as_view(), name="profile"),
    path('login/', LoginView.as_view(template_name='Aeidl/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='Aeidl/login.html'), name='logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
