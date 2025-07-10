# feedback/viewsets.py
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Feedback
from .serializers import FeedbackSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.select_related('job', 'author').all()
    serializer_class = FeedbackSerializer

    permission_classes = [IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    filterset_fields = {
        'job': ['exact'],
        'author': ['exact'],
        'rating': ['exact', 'gte', 'lte'],
    }

    search_fields = ['comment']
    
    ordering_fields = ['created_at', 'rating']
    ordering = ['-created_at']
