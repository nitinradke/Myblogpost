import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','second_project.settings')

import django
django.setup()
## FAKE POP JavaScript

import random
from secondapp.models import AccessRecord,Website,Topic
from faker import Faker
fake = Faker()
topics = ['Marketplace','Social','Search','News']

def get_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for i in range(N):
        fake_url = fake.url()
        fake_date = fake.date()
        fake_name = fake.company()
        # feeding information
        webst = Website.objects.get_or_create(topic=get_topic(),url=fake_url,name=fake_name)[0]

        accs = AccessRecord.objects.get_or_create(name=webst,date=fake_date)[0]

if __name__=='__main__':
    print("populateing")
    populate(20)
    print("completed")
