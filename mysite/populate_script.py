import os, django, random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from faker import Faker
from blog.models import Post
from django.contrib.auth.models import User
from django.utils import timezone


def create_post(N):
    fake = Faker()
    for _ in range(N):
        username = random.randint(1,4)
        title = fake.name()
        status = random.choice(['published', 'draft'])
        Post.objects.create(title=title + " post!!!",
        author = User.objects.get(username='admin'),
        slug = "-".join(title.lower().split()),
        body = fake.text(),
        created = timezone.now(),
        updated=timezone.now(),
        )


create_post(10)
print("DATA IS POPULATED SUCCESSFULLY,")