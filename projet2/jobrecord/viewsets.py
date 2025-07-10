from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import (
    Contract, Skill, Industry,
    Location, JobTitle, Candidate, JobRecord
)
from .serializers import (
    ContractSerializer, SkillSerializer, IndustrySerializer,
    LocationSerializer, JobTitleSerializer,
    CandidateSerializer, JobRecordSerializer
)

class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['type_code', 'description']
    ordering_fields = ['type_code']

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class IndustryViewSet(viewsets.ModelViewSet):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['code', 'name']

class JobTitleViewSet(viewsets.ModelViewSet):
    queryset = JobTitle.objects.all()
    serializer_class = JobTitleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.select_related('location').all()
    serializer_class = CandidateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'email']

class JobRecordViewSet(viewsets.ModelViewSet):
    queryset = JobRecord.objects.select_related(
        'employment_type', 'job_title', 'employee_residence',
        'company_location', 'candidate'
    ).prefetch_related('skills', 'industries').all()
    serializer_class = JobRecordSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = [
        'work_year', 'experience_level', 'employment_type',
        'company_location', 'remote_ratio'
    ]
    search_fields = ['job_title__title']
    ordering_fields = ['salary_in_usd', 'work_year']
    ordering = ['-salary_in_usd']
