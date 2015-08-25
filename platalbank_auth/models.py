#!/usr/bin/python3
# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField(max_length=32)
    room = models.CharField(max_length=128)
