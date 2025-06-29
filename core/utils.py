# Utility functions used in the application (e.g., email, processing)
# core/utils.py

import csv
from io import BytesIO
from django.http import HttpResponse
from reportlab.pdfgen import canvas

def generate_pdf(applications):
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 800, "Visa Applications List")
    y = 780

    for app in applications:
        text = f"{app.applicant_name} - {app.visa_type} - {app.status} - {app.submission_date}"
        p.drawString(100, y, text)
        y -= 20
        if y < 50:
            p.showPage()
            y = 800

    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer

def generate_csv(applications):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="visa_applications.csv"'
    writer = csv.writer(response)
    writer.writerow(['Applicant Name', 'Visa Type', 'Status', 'Submission Date'])

    for app in applications:
        writer.writerow([app.applicant_name, app.visa_type, app.status, app.submission_date])

    return response