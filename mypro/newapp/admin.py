from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display="firstname","lastname","country"

admin.site.register(Member,MemberAdmin)
