from django.contrib import admin
from core.models import PatientAppoint, PatientQuery, Newsletter

class PatientAdmin(admin.ModelAdmin):
    list_display = ('yourname', 'youremail', 'yourmobile', 'yourdoctor', 'yourdate', 'yourtime', 'problem')

admin.site.register(PatientAppoint,PatientAdmin)

class QueryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')

admin.site.register(PatientQuery,QueryAdmin)

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('newemail',)

admin.site.register(Newsletter,NewsletterAdmin)