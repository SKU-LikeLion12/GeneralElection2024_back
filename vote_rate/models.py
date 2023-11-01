from django.db import models

# Create your models here.
class candidate(models.Model):
    name = models.CharField(max_length=128, null=False, primary_key=True)
    total_student_num = models.IntegerField(null=False)
    voted_student_num = models.IntegerField(null=False)
    win = models.CharField(max_length=128, null=True)
    category = models.CharField(max_length=128, null=True)
    time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
        
