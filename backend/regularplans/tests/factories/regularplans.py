import factory
from factory import fuzzy
from faker import Faker

from backend.regularplans.models import RegularPlan
from backend.users.tests.factories.users import UserFactory

fake = Faker()


class RegularPlansFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = RegularPlan

    name = fake.name()
    tar_included = fake.pybool()
    subscription = fake.pyfloat(positive=True)
    cycle = fuzzy.FuzzyChoice(RegularPlan.CYCLE_CHOICES, getter=lambda c: c[0])
    type = fuzzy.FuzzyChoice(RegularPlan.TYPE_CHOICES, getter=lambda c: c[0])
    offer_iva = fake.pybool()
    off_peak_price = fake.pyfloat(positive=True)
    peak_price = fake.pyfloat(positive=True)
    unit = fuzzy.FuzzyChoice(RegularPlan.UNIT_CHOICES, getter=lambda c: c[0])
    valid = fake.pybool()
    publish = fake.pybool()
    vat = fake.pyint(min_value=1, max_value=100)
    owner = factory.SubFactory(UserFactory)