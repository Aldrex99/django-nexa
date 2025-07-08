# import_jobs.py

import os
import csv
import django

# 1. Initialisation Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projet2.settings")
django.setup()

from jobrecord.models import (
    JobTitle, Location, Contract,
    Skill, Industry, Candidate, JobRecord
)

CSV_PATH = "./salaries.csv"

def import_csv():
    created = {
        "job_titles": 0,
        "locations": 0,
        "contracts": 0,
        "candidates": 0,
        "records": 0
    }

    with open(CSV_PATH, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # JobTitle
            jt, jt_created = JobTitle.objects.get_or_create(title=row["job_title"])
            if jt_created: created["job_titles"] += 1

            # Locations pour employee_residence et company_location
            er, er_created = Location.objects.get_or_create(code=row["employee_residence"])
            if er_created: created["locations"] += 1
            cl, cl_created = Location.objects.get_or_create(code=row["company_location"])
            if cl_created: created["locations"] += 1

            # Contract / Employment Type
            ct, ct_created = Contract.objects.get_or_create(
                type_code=row["employment_type"],
                defaults={"description": row.get("employment_type_description", "")}
            )
            if ct_created: created["contracts"] += 1

            # Candidate (si votre CSV contient candidate_name/email/location)
            cand, cand_created = Candidate.objects.get_or_create(
                email=row.get("candidate_email", ""),
                defaults={
                    "name": row.get("candidate_name", ""),
                    "location": er
                }
            )
            if cand_created: created["candidates"] += 1

            # Création ou récupération de JobRecord
            record, rec_created = JobRecord.objects.get_or_create(
                job_title=jt,
                work_year=int(row["work_year"]),
                employee_residence=er,
                defaults={
                    "experience_level": row["experience_level"],
                    "employment_type": ct,
                    "salary": float(row["salary"]),
                    "salary_currency": row["salary_currency"],
                    "salary_in_usd": float(row["salary_in_usd"]),
                    "remote_ratio": int(row["remote_ratio"]),
                    "company_location": cl,
                    "company_size": row["company_size"],
                    "candidate": cand
                }
            )
            if rec_created:
                created["records"] += 1

                # Skills (séparés par ; ou ,)
                if (row.get("skills", None)):
                    for skill_name in row["skills"].split(';'):
                        s, _ = Skill.objects.get_or_create(name=skill_name.strip())
                        record.skills.add(s)

                # Industries
                if (row.get("industries", None)):
                    for industry_name in row["industries"].split(';'):
                        i, _ = Industry.objects.get_or_create(name=industry_name.strip())
                        record.industries.add(i)

            # Fin du traitement de la ligne

    # Affichage du bilan
    print("Import terminé :")
    for k, v in created.items():
        print(f"  • {k} : {v} créé(s)")

if __name__ == "__main__":
    import_csv()
