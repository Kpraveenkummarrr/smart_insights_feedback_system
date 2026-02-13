from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    college_name = models.CharField(max_length=200)
    event_name = models.CharField(max_length=100)
    event_date = models.DateField()
    rating = models.IntegerField()
    message = models.TextField()
    sentiment = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
