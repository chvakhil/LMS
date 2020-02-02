from django.db import models


# Create your models here.
class Users(models.Model):
    USERNAME= models.CharField(max_length=100)
    PASSWORD= models.CharField(max_length=100)
    EMAIL= models.EmailField()
    MOBILE = models.CharField(max_length=10)
    ACCESS_STATUS= models.BooleanField(default=False)

class Leaves(models.Model):
    USERNAME = models.CharField(default='NA',max_length=100)
    TOTAL_ANNUAL_LEAVES = models.IntegerField()
    TOTAL_SICK_LEAVES = models.IntegerField()
    TOTAL_WFH = models.IntegerField()
class AnnualLeaves(models.Model):
    USERNAME = models.CharField(max_length=110,default='NA')
    LEAVE_TYPE = models.CharField(max_length=100)
    LEAVE_START = models.DateField()
    LEAVE_END = models.DateField()
class SickLeaves(models.Model):
    USERNAME = models.CharField(max_length=110,default='NA')
    LEAVE_TYPE = models.CharField(max_length=100)
    LEAVE_START = models.DateField()
    LEAVE_END = models.DateField()
class WorkFromHomes(models.Model):
    USERNAME = models.CharField(max_length=110,default='NA')
    WFH_TYPE = models.CharField(max_length=100)
    WFH_START = models.DateField()
    WFH_END = models.DateField()
    WFH_ADDRESS = models.CharField(max_length=100)