# core/tests/test_views.py
# Unit tests for VisaApplication views and form validation

from django.test import TestCase
from django.urls import reverse
from core.models import VisaApplication
from core.forms import VisaApplicationForm

class VisaApplicationViewsTest(TestCase):
    def setUp(self):
        # Create a sample visa application for testing
        self.application = VisaApplication.objects.create(
            applicant_name='Ali Tester',
            visa_type='Tourist',
            submission_date='2023-12-01',
            status='Pending'
        )

    def test_all_applications_view(self):
        # Check that the main list view loads correctly
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'all_applications.html')
        self.assertContains(response, 'Ali Tester')

    def test_submit_application_view_get(self):
        # Test GET request to the submission form
        response = self.client.get(reverse('submit'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'submit_application.html')

    def test_submit_application_post_valid(self):
        # Test submitting a valid form via POST
        data = {
            'applicant_name': 'New User',
            'visa_type': 'Work',
            'submission_date': '2024-06-01',
            'status': 'Approved'
        }
        response = self.client.post(reverse('submit'), data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful submission
        self.assertEqual(VisaApplication.objects.count(), 2)

    def test_dashboard_view(self):
        # Check that dashboard view loads with context data
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard.html')
        self.assertIn('visa_type_data', response.context)

    def test_pdf_export_view(self):
        # Test export of applications to PDF
        response = self.client.get(reverse('export_pdf'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('application/pdf', response['Content-Type'])

    def test_csv_export_view(self):
        # Test export of applications to CSV
        response = self.client.get(reverse('export_csv'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('text/csv', response['Content-Type'])
        self.assertIn('Ali Tester', response.content.decode())

class VisaApplicationFormTest(TestCase):
    def test_valid_form(self):
        # Test a valid form submission
        form_data = {
            'applicant_name': 'Test Valid',
            'visa_type': 'Student',
            'submission_date': '2024-01-01',
            'status': 'Approved'
        }
        form = VisaApplicationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        # Test an empty (invalid) form submission
        form = VisaApplicationForm(data={})
        self.assertFalse(form.is_valid())
