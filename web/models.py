from django.db import models

# This is an example of a model in Django so that you can see how you can define your own models :D
# DON'T FORGET to run `python manage.py makemigrations` and `python manage.py migrate` after changing this file!!!

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=200)
    founded = models.DateField()
    city = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100)
    publishers = models.ManyToManyField(Publisher, related_name='books')

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.book.title} - {self.rating}/10"
