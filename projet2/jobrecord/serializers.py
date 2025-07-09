from rest_framework import serializers
from .models import (
    Contract, Skill, Industry,
    Location, JobTitle, Candidate, JobRecord
)

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ['id', 'type_code', 'description']

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name']

class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = ['id', 'name']

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['code', 'name']

class JobTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobTitle
        fields = ['id', 'title']

class CandidateSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True)
    location_id = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all(), source='location', write_only=True
    )

    class Meta:
        model = Candidate
        fields = ['id', 'name', 'email', 'location', 'location_id']

class JobRecordSerializer(serializers.ModelSerializer):
    employment_type = ContractSerializer(read_only=True)
    employment_type_id = serializers.PrimaryKeyRelatedField(
        queryset=Contract.objects.all(), source='employment_type', write_only=True
    )

    job_title = JobTitleSerializer(read_only=True)
    job_title_id = serializers.PrimaryKeyRelatedField(
        queryset=JobTitle.objects.all(), source='job_title', write_only=True
    )

    employee_residence = LocationSerializer(read_only=True)
    employee_residence_id = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all(), source='employee_residence', write_only=True
    )

    company_location = LocationSerializer(read_only=True)
    company_location_id = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all(), source='company_location', write_only=True
    )

    candidate = CandidateSerializer(read_only=True)
    candidate_id = serializers.PrimaryKeyRelatedField(
        queryset=Candidate.objects.all(), source='candidate', write_only=True, allow_null=True, required=False
    )

    skills = SkillSerializer(many=True, read_only=True)
    skill_ids = serializers.PrimaryKeyRelatedField(
        queryset=Skill.objects.all(), source='skills', many=True, write_only=True, required=False
    )

    industries = IndustrySerializer(many=True, read_only=True)
    industry_ids = serializers.PrimaryKeyRelatedField(
        queryset=Industry.objects.all(), source='industries', many=True, write_only=True, required=False
    )

    class Meta:
        model = JobRecord
        fields = [
            'id',
            'work_year',
            'experience_level',
            'employment_type', 'employment_type_id',
            'job_title', 'job_title_id',
            'salary', 'salary_currency', 'salary_in_usd',
            'employee_residence', 'employee_residence_id',
            'remote_ratio',
            'company_location', 'company_location_id',
            'company_size',
            'candidate', 'candidate_id',
            'skills', 'skill_ids',
            'industries', 'industry_ids',
        ]
