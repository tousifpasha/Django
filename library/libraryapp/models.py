from django.db import models

# Create your models here.

class Book(models.Model):
    Book_name=models.CharField(max_length=100,help_text="Enter the name of the book")
    Book_price=models.IntegerField(help_text="Enter the price of the book")
    isbn_number=models.CharField(max_length=100)


    def __str__(self):
        return self.Book_name

