from django.db import models
from django.conf import settings

class LegalPerson(models.Model):
    dn = models.CharField(max_length=1024)
    name = models.CharField(max_length=1024) # FIXME FIXME FIXME: Pull from LDAP -- using django-ldapdb?
