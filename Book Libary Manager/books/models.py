from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    description=models.TextField()
    isbn=models.CharField(max_length=13)
    published_date=models.DateField()
    cover=models.ImageField(upload_to='book_cover/',blank=True,null=True)

    def __str__(self):
        return self.title