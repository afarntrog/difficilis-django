from django.db import models

# Create your models here.

class DilemmaModel(models.Model):
    dilemma_part_one = models.CharField(max_length=500)
    dilemma_part_two = models.CharField(max_length=500)


class Reasons(models.Model):
    pass


# TUTORIAL
class Book(models.Model):

    name = models.CharField(max_length=255)
    isbn_number = models.CharField(max_length=13)

    class Meta:
        db_table = 'book'

    def __str__(self):
        return self.name
