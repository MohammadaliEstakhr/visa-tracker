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
    path('', views.all_applications, name='all_applications'),  # Optional: can be removed if redundant

    # Submit a new visa application
    path('submit/', views.submit_application, name='submit_application'),

    # Export all applications as PDF
    path('export/pdf/', views.export_applications_pdf, name='export_pdf'),

    # Export all applications as CSV
    path('export/csv/', views.export_applications_csv, name='export_csv'),

    # View dashboard with charts and statistics
    path('dashboard/', views.dashboard_view, name='dashboard'),
]

# Append REST API URLs to the main URL patterns
urlpatterns += router.urls
