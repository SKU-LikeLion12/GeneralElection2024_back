from rest_framework import serializers
from vote_rate.models import Candidate

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['name', 'rate', 'time']
        

class ALLCandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields =['name', 'rate']
