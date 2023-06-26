from django.conf import settings
from django.db import models
class QA(models.Model):
    'Generated Model'
    qaField = models.BigIntegerField()
    qa2 = models.BigIntegerField(null=True,blank=True,)
class Testing_for_errors(models.Model):
    'Generated Model'
    testing = models.BigIntegerField()
class Test(models.Model):
    'Generated Model'
    test = models.BigIntegerField()
