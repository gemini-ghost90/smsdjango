from django.db import models

# Create your models here.


class Student(models.Model):
    student_number = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    field_of_study = models.CharField(max_length=50)
    gpa = models.FloatField()

    def __str__(self):
        return f'Student: {self.first_name} {self.last_name}'


class Contact(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    contact_number = models.IntegerField()
    email_address = models.EmailField(max_length=50)
    address = models.CharField(max_length=100)
    message = models.CharField(max_length=150)

    def __str__(self):
        return f'Contact: {self.f_name} {self.l_name}'
