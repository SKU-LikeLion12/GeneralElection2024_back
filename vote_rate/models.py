from django.db import models

# 2024 본선거
class Candidate(models.Model):
    name = models.CharField(max_length=128, null=False, primary_key=True)
    rate = models.FloatField(default=0)
    
    def __str__(self):
        return self.name
   
        
class Refresh(models.Model):
    time = models.DateTimeField()
    
    def __str__(self):
        return f'{self.time}'

# 2024 보궐선거
class ByElectionCandidate(models.Model):
    name = models.CharField(max_length=128, null=False, primary_key=True)
    rate = models.FloatField(default=0)
    
    def __str__(self):
        return self.name
   
        
class ByElectionRefresh(models.Model):
    time = models.DateTimeField()
    
    def __str__(self):
        return f'{self.time}'