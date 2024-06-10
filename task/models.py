from django.db import models
from category.models import Category
# Create your models here.
class Task(models.Model):
    task_title = models.CharField(max_length=100)
    task_description = models.TextField()
    task_assign_date = models.DateField(auto_now=False, auto_now_add=False)
    is_completed=models.BooleanField()
    category=models.ManyToManyField(Category)
    def __str__(self):
        return self.task_title