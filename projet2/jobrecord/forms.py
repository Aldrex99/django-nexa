from django import forms
from .models import (
    JobRecord, Contract, JobTitle,
    Location, Candidate, Skill, Industry
)

class JobRecordForm(forms.ModelForm):
    skills     = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={'size': '5'})
    )
    industries = forms.ModelMultipleChoiceField(
        queryset=Industry.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={'size': '5'})
    )
    # sort job_title, employment_type, employee_residence, company_location, candidate
    employment_type = forms.ModelChoiceField(
        queryset=Contract.objects.all().order_by('type_code'),
        required=True,
        empty_label="Select Employment Type",
        widget=forms.Select()
    )
    job_title = forms.ModelChoiceField(
        queryset=JobTitle.objects.all().order_by('title'),
        required=True,
        empty_label="Select Job Title",
        widget=forms.Select()
    )
    employee_residence = forms.ModelChoiceField(
        queryset=Location.objects.all().order_by('code'),
        required=True,
        empty_label="Select Employee Residence",
        widget=forms.Select()
    )
    company_location = forms.ModelChoiceField(
        queryset=Location.objects.all().order_by('code'),
        required=True,
        empty_label="Select Company Location",
        widget=forms.Select()
    )
    candidate = forms.ModelChoiceField(
        queryset=Candidate.objects.all().order_by('name'),
        required=False,
        empty_label="Select Candidate",
        widget=forms.Select()
    )

    class Meta:
        model = JobRecord
        fields = [
            'work_year',
            'experience_level',
            'employment_type',
            'job_title',
            'salary',
            'salary_currency',
            'salary_in_usd',
            'employee_residence',
            'remote_ratio',
            'company_location',
            'company_size',
            'candidate',
            'skills',
            'industries',
        ]
        widgets = {
            'experience_level': forms.TextInput(attrs={'placeholder': 'e.g. SE, MI, EX'}),
            'company_size':     forms.TextInput(attrs={'placeholder': 'e.g. S, M, L, XL'}),
        }
