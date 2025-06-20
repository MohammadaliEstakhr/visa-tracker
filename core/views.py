
from django.shortcuts import render, redirect
from .models import VisaApplication
from .forms import VisaApplicationForm
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.db.models import Count
from datetime import datetime
import csv

# View to display all visa applications
def all_applications(request):
    applications = VisaApplication.objects.all()
    return render(request, 'all_applications.html', {'applications': applications})

# View to handle visa application submission form
def submit_application(request):
    if request.method == 'POST':
        form = VisaApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VisaApplicationForm()
    return render(request, 'submit_application.html', {'form': form})

# View to export all applications to a PDF file
def export_applications_pdf(request):
    applications = VisaApplication.objects.all()
    template = get_template('pdf_template.html')
    html = template.render({'applications': applications})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="visa_applications.pdf"'
    pisa.CreatePDF(html, dest=response)
    return response

# View to export all applications to a CSV file
def export_applications_csv(request):
    applications = VisaApplication.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="visa_applications.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name', 'Visa Type', 'Submission Date', 'Status'])
    for app in applications:
        writer.writerow([app.applicant_name, app.visa_type, app.submission_date, app.status])
    return response

# View to render the dashboard with aggregated application data
def dashboard_view(request):
    # Count of applications by visa type
    visa_type_data = list(VisaApplication.objects.values('visa_type').annotate(count=Count('id')))

    # Count of applications by status
    status_data = list(VisaApplication.objects.values('status').annotate(count=Count('id')))

    # Count of applications submitted each month
    monthly_data = list(
        VisaApplication.objects.extra(select={'month': "strftime('%%Y-%%m', submission_date)"})
        .values('month').annotate(count=Count('id')).order_by('month')
    )

    context = {
        'visa_type_data': visa_type_data,
        'status_data': status_data,
        'monthly_data': monthly_data,
        'datetime': datetime.now()
    }
    return render(request, 'dashboard.html', context)
