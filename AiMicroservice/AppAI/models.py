from django.db import models

# Create your models here.

class Prompt(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    user_id = models.IntegerField(null=False, blank=False)
    question = models.CharField(max_length=1000, null=True, blank=True)
    answer = models.CharField(max_length=1000, null=True, blank=True)



