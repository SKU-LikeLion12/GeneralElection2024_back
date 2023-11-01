from django.contrib import admin
from vote_rate.models import Candidate

admin.site.register(Candidate)

# class CandidateAdmin(admin.ModelAdmin):
#     readonly_fields = ('name', 'total_student_num', 'category', 'time')

# admin.site.register(Candidate, CandidateAdmin)

# 모델 만들고 주석 풀어야함