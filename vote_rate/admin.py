from django.contrib import admin
from vote_rate.models import candidate

# class CandidateAdmin(admin.ModelAdmin):
#     readonly_fields = ('name', 'total_student_num', 'category', 'time')

admin.site.register(candidate)

# class CandidateAdmin(admin.ModelAdmin):
#     readonly_fields = ('name', 'total_student_num', 'category', 'time')

# admin.site.register(candidate, CandidateAdmin)