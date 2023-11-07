from vote_rate.models import Candidate, Refresh
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from vote_rate.serializers import ALLCandidateSerializer, RefreshSerializer


@api_view(['GET'])
def ALLCandidateAPI(request):
    candidate = Candidate.objects.all()
    serializer = ALLCandidateSerializer(candidate, many=True)

    data = {}
    for item in serializer.data:
        data[item['name']] = item['rate']
    
    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
def RefreshAPI(request):
    refresh = Refresh.objects.all().first()
    serializer = RefreshSerializer(refresh)
    
    date_time_str = serializer.data['time']
    date, time = date_time_str.split('T')
    
    data = {}
    data['date'] = date
    data['time'] = time
    
    return Response(data, status=status.HTTP_200_OK)
