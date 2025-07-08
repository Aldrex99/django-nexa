from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from .models import Feedback
from .forms import FeedbackForm
from jobrecord.models import JobRecord

def feedback_list(request, job_id):
    """
    Get all feedbacks for a job and
    allow filtering by minimum rating via GET parameter ?min_rating=3.
    """
    job = get_object_or_404(JobRecord, pk=job_id)
    min_rating = request.GET.get('min_rating')
    qs = job.feedbacks.all()
    if min_rating and min_rating.isdigit():
        qs = qs.filter(rating__gte=int(min_rating))
    return render(request, 'feedback/feedback_list.html', {
        'job': job,
        'feedbacks': qs,
        'min_rating': min_rating or '',
    })

def feedback_create(request, job_id):
    """
    Form to create a new feedback for a job.
    """
    job = get_object_or_404(JobRecord, pk=job_id)
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            fb = form.save(commit=False)
            fb.job    = job
            if not fb.author and request.user.is_authenticated:
                fb.author = request.user
            fb.save()
            return redirect('feedback_list', job_id=job.pk)
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback_form.html', {
        'job': job,
        'form': form,
    })

def feedback_average(request, job_id):
    """
    Calculate and display the average rating for a job.
    """
    job = get_object_or_404(JobRecord, pk=job_id)
    avg = job.feedbacks.aggregate(moy=Avg('rating'))['moy'] or 0
    return render(request, 'feedback/feedback_average.html', {
        'job': job,
        'average_rating': round(avg, 2),
    })
