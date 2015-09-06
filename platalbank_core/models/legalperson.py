from django.db import models
from django.conf import settings

class LegalPerson(models.Model):
    ldap_dn = models.CharField(max_length=1024)
