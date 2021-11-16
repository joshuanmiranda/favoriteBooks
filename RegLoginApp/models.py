from django.db import models
import re, bcrypt

class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name_length"] = "First name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name_length"] = "Last name should be at least 2 characters"
        if len(User.objects.filter(email_address=postData['email_address'])) > 0:
            errors['existingUser'] = "User already registered with that email!"
        Email_Regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not Email_Regex.match(postData['email_address']):
            errors["invalid_email"] = "Invalid Email Address"
        if len(postData['password']) < 8:
            errors["password_length"] = "Password must be at least 8 characters"
        if not postData['password_conf'] == postData['password']:
            errors["password_match"] = "Password did not match confirmation"
        return errors
    def log_validator(self, postData):
        errors = {}
        checkUser = User.objects.filter(email_address = postData['log_email'])
        if len(checkUser) < 1:
            errors['no_email'] = "Invalid Email Address and Password combination"
        elif not bcrypt.checkpw(postData['log_password'].encode(), checkUser[0].password.encode()):
            errors['passwordNoMatch'] = "Invalid Email Address and Password combination"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email_address = models.CharField(max_length=60)
    password = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()