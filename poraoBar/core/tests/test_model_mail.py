from _datetime import datetime

from django.test import TestCase

from poraoBar.core.models import Email

class Modelmailtest(TestCase):
    def setUp(self):
        self.obj = Email(
            mail='mail@gmail.com'
        )
        self.obj.save()
    def test_create(self):
        self.assertTrue(Email.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created_at att"""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('mail@gmail.com', str(self.obj))