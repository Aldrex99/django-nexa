from django.urls import path
from . import views

urlpatterns = [
    path(
      'job/<int:job_id>/feedbacks/page/',
      views.job_feedbacks_page,
      name='feedbacks_page'
    ),
    path('job/<int:job_id>/feedbacks/add/',  views.job_feedback_add_page, name='feedback_add_page'),
]