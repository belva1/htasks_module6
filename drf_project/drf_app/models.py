from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=64, unique=True)
    age = models.IntegerField(default=30)

    def __str__(self):
        return self.name

    """
    self.author_of_books is the callback between the Author and Book models. 
    This field is a QuerySet of books associated with this author.
    """
    def get_id_of_books(self):
        return list(self.author_of_books.values_list('id', flat=True))


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name='author_of_books', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title