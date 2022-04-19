from django.db import models

# Create your models here.
class StudentDetails(models.Model):
  fullname = models.CharField(max_length=50)
  address = models.TextField(blank=True)
  age = models.IntegerField(blank=True)
  gender = models.CharField(max_length=6,blank=True)
  standard = models.CharField(max_length=30,blank=True)
  contact_no = models.CharField(max_length=15,blank=True)

  def __str__(self):
    return self.fullname


