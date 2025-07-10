from django.shortcuts import render, get_object_or_404
from jobrecord.models import JobRecord
from django.db import models
from django.contrib.auth.models import User

def job_feedbacks_page(request, job_id):
    job   = get_object_or_404(JobRecord, pk=job_id)
    # Calculating the average rating for the job
    average_rating = (job.feedbacks.aggregate(
        avg_rating=models.Avg('rating')
    )['avg_rating'] or 0).__round__(2)

    return render(request, 'feedback/job_feedbacks.html', {
        'job': job,
        'average_rating': average_rating,
    })

def job_feedback_add_page(request, job_id):
    """
    Page séparée pour ajouter un feedback via JS/API.
    """
    job   = get_object_or_404(JobRecord, pk=job_id)
    users = User.objects.all()
    return render(request, 'feedback/job_feedback_add.html', {
        'job': job,
        'users': users,
    })