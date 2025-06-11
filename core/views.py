from django.shortcuts import render, redirect
from django.contrib import messages
from .models import VisaApplication
from .forms import VisaApplicationForm
from datetime import datetime
from django.http import HttpResponse
from django.template.loader import get_template
import csv
from xhtml2pdf import pisa
from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.contrib.auth.decorators import login_required

# نمایش همه درخواست‌ها
@login_required
def all_applications(request):
    applications = VisaApplication.objects.all()

    search_query = request.GET.get('search')
    status_filter = request.GET.get('status')

    if search_query:
        applications = applications.filter(applicant_name__icontains=search_query) | applications.filter(visa_type__icontains=search_query)

    if status_filter:
        applications = applications.filter(status=status_filter)

    return render(request, 'all_applications.html', {'applications': applications})

# ثبت درخواست جدید
@login_required
def submit_application(request):
    if request.method == 'POST':
        form = VisaApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Visa application submitted successfully!')
            return redirect('home')
    else:
        form = VisaApplicationForm()
    return render(request, 'submit_application.html', {'form': form})

# خروجی PDF
@login_required
def export_applications_pdf(request):
    applications = VisaApplication.objects.all()
    template = get_template('pdf_template.html')
    html = template.render({'applications': applications})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="visa_applications.pdf"'
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

# خروجی CSV
@login_required
def export_applications_csv(request):
    applications = VisaApplication.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="visa_applications.csv"'
    writer = csv.writer(response)
    writer.writerow(['Applicant', 'Visa Type', 'Submission Date', 'Status'])
    for app in applications:
        writer.writerow([app.applicant_name, app.visa_type, app.submission_date, app.status])
    return response

# داشبورد با نمودار
@login_required
def dashboard_view(request):
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    visa_type_data = VisaApplication.objects.values('visa_type').annotate(count=Count('id'))
    status_data = VisaApplication.objects.values('status').annotate(count=Count('id'))

    monthly_data = VisaApplication.objects.annotate(
        month=TruncMonth('submission_date')
    ).values('month').annotate(count=Count('id')).order_by('month')

    # تبدیل تاریخ‌ها به رشته برای نمایش در JS
    monthly_data = [
        {'month': item['month'].strftime('%Y-%m-%d'), 'count': item['count']}
        for item in monthly_data
    ]

    context = {
        'datetime': current_datetime,
        'visa_type_data': list(visa_type_data),
        'status_data': list(status_data),
        'monthly_data': monthly_data,
    }

    return render(request, 'dashboard.html', context)
