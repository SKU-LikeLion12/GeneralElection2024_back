from django.db import models

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=128, null=False, primary_key=True)
    rate = models.FloatField(default=0)
    
    def __str__(self):
        return self.name
   
        
class Refresh(models.Model):
    time = models.DateTimeField()
    
    def __str__(self):
        return f'{self.time}'