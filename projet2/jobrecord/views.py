from django.shortcuts import render
from django.db.models import Avg
from .models import JobRecord

def dashboard(request):
    total_jobs = JobRecord.objects.count()

    avg_data = JobRecord.objects.aggregate(avg_usd=Avg('salary_in_usd'))
    avg_salary = avg_data['avg_usd'] or 0

    res_codes = set(
        JobRecord.objects
                 .exclude(employee_residence__isnull=True)
                 .values_list('employee_residence__code', flat=True)
    )
    comp_codes = set(
        JobRecord.objects
                 .exclude(company_location__isnull=True)
                 .values_list('company_location__code', flat=True)
    )
    num_countries = len(res_codes.union(comp_codes))

    return render(request, 'jobs/dashboard.html', {
        'total_jobs': total_jobs,
        'avg_salary': avg_salary,
        'num_countries': num_countries,
    })
