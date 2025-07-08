from django.db import models

class Contract(models.Model):
    type_code   = models.CharField(max_length=5, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.type_code} – {self.description}"

class Skill(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Industry(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Candidate(models.Model):
    name     = models.CharField(max_length=200, null=True, blank=True)
    email    = models.EmailField(unique=True, null=True, blank=True)
    location = models.ForeignKey(
        "Location",
        on_delete=models.SET_NULL,
        null=True,
        related_name="candidates"
    )

    def __str__(self):
        return self.name

class JobTitle(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

class Location(models.Model):
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.code

class JobRecord(models.Model):
    work_year        = models.IntegerField()
    experience_level = models.CharField(max_length=5)
    employment_type  = models.ForeignKey(
        Contract,
        on_delete=models.PROTECT,
        related_name="jobrecords"
    )
    job_title        = models.ForeignKey(
        JobTitle,
        on_delete=models.CASCADE,
        related_name="jobrecords"
    )
    salary           = models.FloatField()
    salary_currency  = models.CharField(max_length=10)
    salary_in_usd    = models.FloatField()
    employee_residence = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        related_name="jobs_as_resident"
    )
    remote_ratio     = models.IntegerField()
    company_location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        related_name="jobs_as_company"
    )
    company_size     = models.CharField(max_length=5)

    # Relations ManyToMany for skills and industries
    skills   = models.ManyToManyField(Skill,   related_name="jobrecords", blank=True, null=True)
    industries = models.ManyToManyField(Industry, related_name="jobrecords", blank=True, null=True)
    candidate  = models.ForeignKey(
        Candidate,
        on_delete=models.SET_NULL,
        null=True,
        related_name="jobrecords"
    )

    class Meta:
        unique_together = (
            ("job_title", "work_year", "employee_residence"),
        )

    def __str__(self):
        return f"{self.job_title} ({self.work_year}) – {self.employee_residence}"
