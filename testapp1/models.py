from django.db import models

# Create your models here.
class CustomManager(models.Manager):
    def get_queryset(self):
        qs = super().get_queryset().order_by('eno')
        return qs
    def get_emp_sal_range(self,minsal,maxsal):
        qs = super().get_queryset().filter(esal__range=(minsal,maxsal))
        return qs
    def get_emp_sorted_by(self,param):
        qs = super().get_queryset().order_by(param)
        return qs

class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=30)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=30)
    objects = CustomManager()

