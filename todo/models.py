from django.db import models
from datetime import date
# Create your models here.


class ToDo(models.Model):
    todo_text = models.CharField(max_length=300)
    complete = models.BooleanField(default=False)
    assigned_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)
    completed_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.todo_text

    def add_task(self, text, due_date):
        self.todo_text = text
        self.due_date = due_date

    def complete_task(self):
        self.complete = True
        self.completed_date = date.today
