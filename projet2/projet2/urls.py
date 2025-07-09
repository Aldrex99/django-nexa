from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',         include('jobrecord.urls', namespace='jobs')),
    path('feedback/', include('feedback.urls')),

    path('api/jobs/',     include('jobrecord.api_urls')),
    path('api/feedback/', include('feedback.api_urls')),
]
