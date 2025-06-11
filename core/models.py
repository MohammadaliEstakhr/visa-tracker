from django.db import models

class VisaApplication(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )

    applicant_name = models.CharField(max_length=100)
    visa_type = models.CharField(max_length=100)
    submission_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    document = models.FileField(upload_to='documents/', blank=True, null=True)

    def __str__(self):
        return f"{self.applicant_name} - {self.visa_type}"
