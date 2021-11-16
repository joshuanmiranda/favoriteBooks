from django.db import models
from RegLoginApp.models import *

class BookManager(models.Manager):
    def book_valid(self, postData):
        errors = {}
        if len(postData['title']) < 1:
            errors["title_length"] = "Book title required"
        if len(postData['description']) < 5:
            errors["description_length"] = "Description should be at least 5 characters"
        return errors

class Book(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded", on_delete=models.CASCADE)
    users_who_like = models.ManyToManyField(User, related_name="liked_book")