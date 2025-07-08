from django.shortcuts import render
from django.db.models import Count, Avg
from django.core.paginator import Paginator
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

def job_list(request):
    qs = (
        JobRecord.objects
        .annotate(
            feedback_count=Count('feedbacks'),
            feedback_avg=Avg('feedbacks__rating'),
        )
        .order_by('-work_year', 'job_title__title')
    )
    paginator = Paginator(qs, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    for job in page_obj:
        job.feedback_count = job.feedbacks.count()
        job.feedback_avg = job.feedbacks.aggregate(moy=Avg('rating'))['moy'] or 0
        print(f"Job: {job.job_title.title}, "
              f"Feedbacks: {job.feedback_count}, "
              f"Avg Rating: {job.feedback_avg:.2f}")
    
    return render(request, 'jobs/job_list.html', {
        'jobs': page_obj,
        'page_obj': page_obj,
    })
