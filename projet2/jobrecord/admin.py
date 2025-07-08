# jobs/admin.py

from django.contrib import admin
from .models import (
    Contract, Skill, Industry,
    Candidate, JobTitle, Location,
    JobRecord
)

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ("type_code", "description")
    search_fields = ("type_code", "description")

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "location")
    search_fields = ("name", "email")
    list_filter = ("location",)

@admin.register(JobTitle)
class JobTitleAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("code", "name")
    search_fields = ("code", "name")

@admin.register(JobRecord)
class JobRecordAdmin(admin.ModelAdmin):
    list_display = (
        "job_title", "work_year", "employment_type",
        "employee_residence", "company_location", "salary_in_usd"
    )
    list_filter = ("work_year", "employment_type", "remote_ratio")
    search_fields = ("job_title__title",)
    filter_horizontal = ("skills", "industries")
