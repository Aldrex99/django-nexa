from django.urls import path
from . import views

urlpatterns = [
    path('job/<int:job_id>/feedbacks/',      views.feedback_list,    name='feedback_list'),
    path('job/<int:job_id>/feedbacks/add/',  views.feedback_create,  name='feedback_create'),
    path('job/<int:job_id>/feedbacks/avg/',  views.feedback_average, name='feedback_average'),
]