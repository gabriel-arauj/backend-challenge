import factory
from faker import Faker

from backend.users.models import User

fake = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    username = fake.name()
    email = fake.email()
    password = factory.PostGenerationMethodCall('set_password', 'password')

