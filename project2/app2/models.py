from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_id= models.AutoField(primary_key=True)
    emp_name= models.CharField(max_length=100)
    emp_contact= models.IntegerField(unique=True)
    emp_salary= models.FloatField()

    
