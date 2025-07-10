from django.shortcuts import render, get_object_or_404
from jobrecord.models import JobRecord

def job_feedbacks_page(request, job_id):
    job   = get_object_or_404(JobRecord, pk=job_id)
    return render(request, 'feedback/job_feedbacks.html', {
        'job': job,
    })
