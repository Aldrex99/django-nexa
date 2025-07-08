import os
import django

# Django initialization
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projet2.settings")
django.setup()

from django.db.models import Avg, Count, Q
from jobrecord.models import JobRecord

def run_reports():
    lines = []

    # Top 5 des Job Titles (salaire moyen en USD)
    lines.append("Top 5 des Job Titles (salaire moyen en USD) :\n")
    top5 = (
        JobRecord.objects
                 .values("job_title__title")
                 .annotate(avg_usd=Avg("salary_in_usd"))
                 .order_by("-avg_usd")[:5]
    )
    for i, rec in enumerate(top5, start=1):
        lines.append(f"  {i}. {rec['job_title__title']} — {rec['avg_usd']:.2f} USD\n")
    lines.append("\n")

    # Average salary by experience level
    lines.append("Salaire moyen par niveau d’expérience :\n")
    avg_by_exp = (
        JobRecord.objects
                 .values("experience_level")
                 .annotate(avg_usd=Avg("salary_in_usd"))
                 .order_by("experience_level")
    )
    for rec in avg_by_exp:
        lvl = rec["experience_level"]
        lines.append(f"  • {lvl} : {rec['avg_usd']:.2f} USD\n")
    lines.append("\n")

    # Number of jobs by company location
    lines.append("Nombre de jobs par company_location :\n")
    count_by_loc = (
        JobRecord.objects
                 .values("company_location__code")
                 .annotate(nb=Count("id"))
                 .order_by("-nb")
    )
    for rec in count_by_loc:
        loc = rec["company_location__code"]
        lines.append(f"  • {loc} : {rec['nb']}\n")
    lines.append("\n")

    # Ratio of 100% remote jobs
    total = JobRecord.objects.count()
    remote100 = JobRecord.objects.filter(remote_ratio=100).count()
    ratio = (remote100 / total * 100) if total else 0
    lines.append(f"Ratio de jobs 100% remote : {remote100}/{total} ({ratio:.2f}%)\n")

    # Writing to file
    output_path = "report.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.writelines(lines)

    # Output to console
    print("".join(lines))
    print(f"\nRapport enregistré dans `{output_path}`")

if __name__ == "__main__":
    run_reports()
