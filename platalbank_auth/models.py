#!/usr/bin/python3
# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField(max_length=32)
    room = models.CharField(max_length=128)


    def get_ro_legalpeople(self):
        """return all legal people this user has read-only permissions on"""
        # TODO: LDAP Stuff
        return tuple()

    def get_rw_legalpeople(self):
        """return all legal people this user has read-write permissions on"""
        # TODO: LDAP stuff
        return tuple()
