# Generated by Django 5.2.4 on 2025-07-08 07:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_code', models.CharField(max_length=5, unique=True)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5, unique=True)),
                ('name', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='candidates', to='jobrecord.location')),
            ],
        ),
        migrations.CreateModel(
            name='JobRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_year', models.IntegerField()),
                ('experience_level', models.CharField(max_length=5)),
                ('salary', models.FloatField()),
                ('salary_currency', models.CharField(max_length=10)),
                ('salary_in_usd', models.FloatField()),
                ('remote_ratio', models.IntegerField()),
                ('company_size', models.CharField(max_length=5)),
                ('candidate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='jobrecords', to='jobrecord.candidate')),
                ('employment_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='jobrecords', to='jobrecord.contract')),
                ('industries', models.ManyToManyField(blank=True, related_name='jobrecords', to='jobrecord.industry')),
                ('job_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobrecords', to='jobrecord.jobtitle')),
                ('company_location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='jobs_as_company', to='jobrecord.location')),
                ('employee_residence', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='jobs_as_resident', to='jobrecord.location')),
                ('skills', models.ManyToManyField(blank=True, related_name='jobrecords', to='jobrecord.skill')),
            ],
            options={
                'unique_together': {('job_title', 'work_year', 'employee_residence')},
            },
        ),
    ]
