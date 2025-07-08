from django.db import models
from django.utils import timezone
from jobrecord.models import JobRecord
from django.contrib.auth import get_user_model

User = get_user_model()

class Feedback(models.Model):
    job          = models.ForeignKey(
        JobRecord,
        on_delete=models.CASCADE,
        related_name='feedbacks'
    )
    author       = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='feedbacks'
    )
    comment      = models.TextField()
    rating       = models.PositiveSmallIntegerField()
    created_at   = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f"Feedback {self.pk} - {self.rating}/5 pour {self.job}"
