from django.db import models

# Create your models here.
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Course(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class FormEntry(models.Model):
    name = models.CharField(max_length=100)

    dob = models.DateField()
    age = models.IntegerField()
    # GENDER_CHOICES = [
    #     ('Male', 'Male'),
    #     ('Female', 'Female'),
    #     ('Other', 'Other'),
    # ]
    gender = models.CharField(max_length=10,)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    PURPOSE_CHOICES = [
        ('Enquiry', 'Enquiry'),
        ('Place Order', 'Place Order'),
        ('Return', 'Return'),
    ]
    purpose = models.CharField(max_length=100, choices=PURPOSE_CHOICES)
    materials_provided = models.ManyToManyField(Material)
    def __str__(self):
        return self.name
