from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.job_create, name='job_create'),
]