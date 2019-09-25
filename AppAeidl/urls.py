from django.urls import path, include
from rest_framework.routers import DefaultRouter
from AppAeidl.views import PatientView, MedicView, AnalisiView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'patient', PatientView)
router.register(r'medic', MedicView)
router.register(r'analisis', AnalisiView)

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token_refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
