import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project1.settings')

import django
django.setup()

from first_app.models import info_table
from faker import Faker
fake = Faker()
import random

sections = [ 'A','B','C']
Semesters = [i for i in range(8)]

def populate(N=20):
    for i in range(N):
        rollno = i
        name = fake.name()
        age = random.randrange(18,24)
        Semester = random.choice(Semesters)
        Section = random.choice(sections)
        acc = info_table.objects.get_or_create(rollno = rollno,name= name,Age = age,Semester = Semester,Section = Section)

if __name__ == "__main__":
    print("populating")
    populate(30)
    print("success")
