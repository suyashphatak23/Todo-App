from django.db import models

class Todo(models.Model):
    header = models.CharField(max_length=50, blank=False)
    content = models.CharField(max_length=200, blank=False)
    isCompleted = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.header