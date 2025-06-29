# Database model definition for visa application data
from django.db import models

# Model to store visa application details
class VisaApplication(models.Model):
    # Status options for the visa application
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )

    # Name of the applicant
    applicant_name = models.CharField(max_length=100)

    # Type of visa being applied for
    visa_type = models.CharField(max_length=100)

    # Date when the application was submitted
    submission_date = models.DateField()

    # Current status of the application
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    # Uploaded document (optional)
    document = models.FileField(upload_to='documents/', blank=True, null=True)

    # String representation of the model instance
    def __str__(self):
        return f"{self.applicant_name} - {self.visa_type}"