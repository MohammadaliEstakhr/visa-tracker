from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .api import VisaApplicationViewSet

router = DefaultRouter()
router.register(r'api/applications', VisaApplicationViewSet, basename='application')

urlpatterns = [
    path('', views.all_applications, name='home'),
    path('', views.all_applications, name='all_applications'),
    path('submit/', views.submit_application, name='submit_application'),
    path('export/pdf/', views.export_applications_pdf, name='export_pdf'),
    path('export/csv/', views.export_applications_csv, name='export_csv'),
    path('dashboard/', views.dashboard_view, name='dashboard'),

]

urlpatterns += router.urls