from django.test import TestCase
from django.utils import timezone
from data_entry_app.models import HealthInstitution, Profession, User, Event


class HealthInstitutionTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User(
            password="stacydebra",
            username="Stacy",
            first_name="Stacy",
            last_name="Debra",
            email="",
        )
        user.save()
        HealthInstitution.objects.create(
            name="Mbagathi",
            phone_number="+247987088",
            speciality="Gynaecology",
            location="Nairobi",
            created_by=user,
            date_created=timezone.now(),
        )

    def test_health_institution_label(self):
        health_institution = HealthInstitution.objects.get(id=1)
        field_label = health_institution._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_name_max_length(self):
        health_institution = HealthInstitution.objects.get(id=1)
        max_length = health_institution._meta.get_field("name").max_length
        self.assertEqual(max_length, 50)


class ProfessionTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User(
            password="stacydebra",
            username="Stacy",
            first_name="Stacy",
            last_name="Debra",
            email="",
        )
        user.save()
        Profession.objects.create(
            name="Medicine",
            description="Female reproductive health",
            occupation="Gynaecology",
            created_by=user,
            date_created=timezone.now(),
        )

    def test_profession_label(self):
        profession = Profession.objects.get(id=1)
        field_label = profession._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_name_max_length(self):
        profession = Profession.objects.get(id=1)
        max_length = profession._meta.get_field("name").max_length
        self.assertEqual(max_length, 50)


class EventTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User(
            password="stacydebra",
            username="Stacy",
            first_name="Stacy",
            last_name="Debra",
            email="",
        )
        user.save()
        Event.objects.create(
            event_name="ATS",
            location="Nairobi",
            description="An event for tech professionals to connect",
            event_date=timezone.now(),
            created_by=user,
            date_created=timezone.now(),
        )

    def test_event_label(self):
        event = Event.objects.get(id=1)
        field_label = event._meta.get_field("event_name").verbose_name
        self.assertEqual(field_label, "event_name")

    def test_event_name_max_length(self):
        event = Event.objects.get(id=1)
        max_length = event._meta.get_field("event_name").max_length
        self.assertEqual(max_length, 30)
