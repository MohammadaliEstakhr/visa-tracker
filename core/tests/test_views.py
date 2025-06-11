from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from core.models import VisaApplication

class VisaApplicationViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass123')
        self.client.login(username='testuser', password='testpass123')

    def test_home_view_logged_in(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_submit_application_view(self):
        data = {
            'applicant_name': 'Ali Estakhr',
            'visa_type': 'Graduate',
            'submission_date': '2025-06-10',
            'status': 'Pending'
        }
        response = self.client.post(reverse('submit_application'), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(VisaApplication.objects.count(), 1)
