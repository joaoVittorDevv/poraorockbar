from django.db import models

class Email(models.Model):

    mail = models.EmailField('e-mail')
    created_at = models.DateTimeField('criado em',auto_now_add=True)

    def __str__(self):
        return self.mail
