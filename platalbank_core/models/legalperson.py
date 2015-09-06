from django.db import models
from django.conf import settings

class LegalPerson(models.Model):
    dn = models.CharField(max_length=1024)
    name = models.CharField(max_length=1024) # FIXME FIXME FIXME: Pull from LDAP -- using django-ldapdb?

    def may_access(self, user):
        """whether a user may read the details of this legalperson's accounts.
roughly read-only permissions
"""
        # TODO: LDAP stuff
        return True

    def may_modify(self, user):
        """whether a user can add new trasactions to events owned by this legalperson.
roughly read-write permissions
"""
        # TODO: LDAP stuff
        return True

