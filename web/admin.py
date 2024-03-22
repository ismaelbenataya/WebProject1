from django.contrib import admin

# This is how you can register your models with the Django admin so that you can manage them from the admin interface

from .models import Author, Publisher, Book, Review

admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Review)
