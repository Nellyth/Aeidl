from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from Aeidl import settings
from AppAeidl.views import Home, MedicListView, MedicCreateView, MedicUpdateView, MedicDeleteView, PacienteListView, \
    PacienteCreateView, PacienteUpdateView, PacienteDeleteView, ProfileUpdateUser

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('medic/', MedicListView.as_view(), name="medic_list"),
    path('medic_create/', MedicCreateView.as_view(), name="medic_create"),
    path('medic_update/<int:pk>/', MedicUpdateView.as_view(), name="medic_update"),
    path('medic_erase/<int:pk>/', MedicDeleteView.as_view(), name="medic_erase"),
    path('paciente_/', PacienteListView.as_view(), name="paciente_list"),
    path('paciente_create/', PacienteCreateView.as_view(), name="paciente_create"),
    path('paciente_update/<int:pk>/', PacienteUpdateView.as_view(), name="paciente_update"),
    path('paciente_erase/<int:pk>/', PacienteDeleteView.as_view(), name="paciente_erase"),
    path('profile/<int:pk>/', ProfileUpdateUser.as_view(), name="profile"),
    path('login/', LoginView.as_view(template_name='Aeidl/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='Aeidl/login.html'), name='logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
