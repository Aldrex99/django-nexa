import os
import django
import random

# Django initialization
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projet2.settings')
django.setup()

from django.contrib.auth import get_user_model
from jobrecord.models import JobRecord
from feedback.models import Feedback

User = get_user_model()

def main():
    users = list(User.objects.all())
    if not users:
        print("❌ Aucun utilisateur trouvé. Créez d'abord au moins un User.")
        return

    total_created = 0
    for job in JobRecord.objects.all():
        # Number of feedbacks to create for this job
        n = random.randint(3, 8)
        for i in range(n):
            author  = random.choice(users)
            rating  = random.randint(1, 5)
            comment = (
                f"Avis auto #{i+1} pour '{job.job_title}' " 
                f"({rating}/5) généré le {django.utils.timezone.now().date()}"
            )
            Feedback.objects.create(
                job=job,
                author=author,
                rating=rating,
                comment=comment
            )
            total_created += 1

    print(f"✅ Création terminée : {total_created} feedbacks ajoutés.")

if __name__ == '__main__':
    main()
