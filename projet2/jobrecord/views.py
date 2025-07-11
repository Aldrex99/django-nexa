from django.shortcuts import render
from django.db.models import Count, Avg
from django.core.paginator import Paginator
from .models import JobRecord
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import JobRecordForm

@login_required
def dashboard(request):
    return render(request, 'jobs/dashboard.html')

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

@login_required
def job_create(request):
    if request.method == 'POST':
        form = JobRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jobs:job_list')
    else:
        form = JobRecordForm()
    return render(request, 'jobs/job_create.html', {'form': form})
