from django.test import TestCase

from poraoBar.core.forms import EmailForm


class EmailFormTest(TestCase):
    def setUp(self):

        self.form = EmailForm()

    def test_form_has_fields(self):

        expected = ['mail']
        self.assertSequenceEqual(expected, list(self.form.fields))

class EmailMessage(TestCase):

    def setUp(self):
        self.data = dict(mail='mail@gmail.com')

    def test_success_message(self):
        response = self.client.post('/', self.data, follow=True)
        self.assertContains(response, 'Inscrição realizada com sucesso')