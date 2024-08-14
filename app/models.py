from django.db import models

# Create your models here.

class Student(models.Model):
    sid=models.IntegerField(primary_key=True)
    sname=models.CharField(max_length=100)
    sage=models.IntegerField()
    em=models.EmailField()

    def __str__(self):
        return str(self.sname)