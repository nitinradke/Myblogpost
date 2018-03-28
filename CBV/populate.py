import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","CBV.settings")

import django
django.setup()


from first_app.models import School
from faker import Faker
fake = Faker()
import random

l = [i for i in range(40,75)]

def populate(N=30):
    for i in range(N):
        name = fake.name()
        age = random.choice(l)
        city = fake.city()
        acc = School.objects.get_or_create(name=name,age = age,city = city)

if __name__ == "__main__":
    print("populating")
    populate(20)
    print("completed")
