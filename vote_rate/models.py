from django.db import models

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=128, null=False, primary_key=True)
    rate = models.FloatField(default=0)
    category = models.CharField(max_length=128, null=True, blank=True)
    time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
        
