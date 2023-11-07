from rest_framework import serializers
from vote_rate.models import Candidate, Refresh


class ALLCandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['name', 'rate']
    

class RefreshSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refresh
        fields = ['time']
