from __future__ import unicode_literals
from django.db import models
import re
    

# Create your models here.
class PWmanager(models.Manager):
    def Pass_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # email from registration
        if not EMAIL_REGEX.match(postData['needs_revision']):
            errors['email'] = "Invalid email address"
        # this needs to be the phone number in the reg page 
        if len(postData['needs_revision']) < 10:
            errors['number'] = "your number is "
        # password from the registration
        if len(postData['needs_revision']) < 8:
            errors['password'] = "your password is too short"
        # first name from registration
        if len(postData['needs_revision']) < 3:
            errors['firs_name']= "your first name must be entered and at least 3 letters long."
        # last name from the registration
        if len(postData['needs_revision']) < 3:
            errors['last_name'] = "your last name must be entered and at least 3 letters long"
        # email from the registration page this tests for weather the email exists this is how I prevent duplicate users
        for user in Users.objects.all():
            if user.email == postData['needs_revision']:
                errors['existance'] = "this email is already in use."
        return errors

class Users(models.Model):
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=48)
    last_name = models.CharField(max_length=48)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    objects = PWmanager()
    def __repr__(self):
        return f"\n{100*'*'}\nID: {self.id}\n{self.email} : {self.password}\nfirst_name : {self.first_name}\nlast_name : {self.last_name}\n{100*'*'}"

class prospectManager(models.Manager):
    def pros_validator(self, postData):
        # this is for the prospects name
        errors = {}
        if postData['needs_revision'] < 3:
            errors['name'] = "must have at leaset 3 characters in the name field"

class Prospects(models.Model):
    name = models.CharField(max_length=255)
    forlowup = DateField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=255)
    step = models.CharField(max_length=255)
    user = models.ManyToManyField(Users, related_name="Prospects")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class Notes(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    notes = models.TextField()
    Prospect = models.ForeignKey(Prospects, related_name="notes")

