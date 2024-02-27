from django.db import models

# Create your models here.
class Question(models.Model):
    category = models.CharField(max_length=255)
    question_text = models.TextField()
    correct_answer = models.CharField(max_length=255)
    options = models.JSONField()

    def __str__(self):
        return self.question_text
