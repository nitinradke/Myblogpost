import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','third_project.settings')

import django
django.setup()

from first_app.models import info
from faker import Faker
fake = Faker()

def populate(N=20):
    for i in range(N):
        fake_first_name = fake.first_name()
        fake_last_name = fake.last_name()
        fake_email = fake.email()

        accs = info.objects.get_or_create(First_name=fake_first_name,Last_name=fake_last_name,email=fake_email)


if __name__ == '__main__':
    print('populating')
    populate(30)
    print('completed')
