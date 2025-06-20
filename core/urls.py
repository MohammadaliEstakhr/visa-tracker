# core/urls.py
# URL routing configuration for core app views and API endpoints

from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .api import VisaApplicationViewSet

# DRF router for RESTful API endpoints
router = DefaultRouter()
router.register(r'api/applications', VisaApplicationViewSet, basename='application')

# URL patterns for the core application
urlpatterns = [
    # Home and list of all visa applications
    path('', views.all_applications, name='home'),
    path('all/', views.all_applications, name='all_applications'),

    # Submit a new visa application
    path('submit/', views.submit_application, name='submit'),  # ✅ updated name for test compatibility

    # Export all applications as PDF
    path('export/pdf/', views.export_applications_pdf, name='export_pdf'),

    # Export all applications as CSV
    path('export/csv/', views.export_applications_csv, name='export_csv'),

    # Dashboard with statistics and charts
    path('dashboard/', views.dashboard_view, name='dashboard'),
]

# Include REST API endpoints
urlpatterns += router.urls
