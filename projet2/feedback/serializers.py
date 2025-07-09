from rest_framework import serializers
from .models import Feedback
from jobrecord.serializers import JobRecordSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class FeedbackSerializer(serializers.ModelSerializer):
    job = JobRecordSerializer(read_only=True)
    job_id = serializers.PrimaryKeyRelatedField(
        queryset=Feedback._meta.get_field('job').related_model.objects.all(),
        source='job',
        write_only=True
    )

    author = AuthorSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='author',
        write_only=True
    )

    class Meta:
        model = Feedback
        fields = [
            'id',
            'job', 'job_id',
            'author', 'author_id',
            'comment',
            'rating',
            'created_at',
        ]
        read_only_fields = ['created_at']
