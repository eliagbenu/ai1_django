from django.db import models

# Create your models here.

class Bank(models.Model):
    bank_name = models.CharField(max_length=30)
    website_address = models.URLField()

    def __unicode__(self):
        return self.bank_name


