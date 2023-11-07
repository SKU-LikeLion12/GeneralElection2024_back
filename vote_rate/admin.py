from django.contrib import admin
from vote_rate.models import Candidate, Refresh

class CandidateAdmin(admin.ModelAdmin):
    readonly_fields = ['name']

    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Candidate, CandidateAdmin)


class RefreshAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Refresh, RefreshAdmin)

# admin.site.register(Refresh)
# admin.site.register(Candidate)