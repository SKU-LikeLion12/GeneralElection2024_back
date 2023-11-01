from django.shortcuts import render
from vote_rate.models import Candidate
from django.http import HttpResponse


def test(request, name):
    candidate = Candidate.objects.get(name=name)
    return HttpResponse(candidate.name)
