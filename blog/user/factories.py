import factory.fuzzy
from .models import User
from factory.faker import Faker


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    username = factory.Faker('email')
    password = factory.Faker('password', length=12)
    age = factory.Faker('random_int', min=18, max=100)
