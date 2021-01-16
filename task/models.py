import datetime
from django.db import models
from django.db.models.signals import pre_save
# Create your models here.
type_choice=(
             ('important','important'),
             ('regular','regular'),
             ('done','done'),
             )


class Tasks(models.Model):
    # order_date = models.DateField(default=datetime.date.today)
    complete_date = models.DateField(default=datetime.date.today)
    subject =models.CharField(max_length=99)
    detail =models.TextField(max_length=999)
    status =models.CharField(max_length=99,choices=type_choice)

    def __str__(self):
        return f'Task of {self.complete_date}---{self.subject}'




