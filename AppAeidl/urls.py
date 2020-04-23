from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from AppAeidl.views import PatientView, MedicView, AnalisisView, download_file, EntityView, AppointmentView, StudyView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
#
# router = DefaultRouter()
# router.register(r'patient', PatientView)
# router.register(r'medic', MedicView)
# router.register(r'analisis', AnalisisView)
# router.register(r'entity', EntityView)
# router.register(r'appointment', AppointmentView)
# router.register(r'study', StudyView)
#
from Aeidl import settings
from AppAeidl.views import Home

urlpatterns = [
    # path('', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token_refresh', TokenRefreshView.as_view(), name='token_refresh'),
    # path('', include(router.urls)),
    # path('download_file', download_file, name='download_file')
    path('', Home.as_view(), name="home"),
    path('login/', LoginView.as_view(template_name='Aeidl/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='Aeidl/login.html'), name='logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
