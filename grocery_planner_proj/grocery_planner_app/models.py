from django.db import models
import re

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if postData['pw'] != postData['confpw']:
            errors['pass'] = 'Nope, your passwords did not match. Try again.'
        if len(postData['user_name']) < 5:
            errors['user'] = 'User name must be more than 5 characters'
        return errors

class User(models.Model):
    user_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    password = models.CharField(max_length=50)
    objects = UserManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


