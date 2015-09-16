from django.contrib import admin

from .models import IsIt, Doctor, Patient

class PatientAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Данные пациента', {'fields': ['first_name', 'last_name']}),
        ('Время приема', {'fields': ['dt', 'tm']}),
        ('Лечащий врач', {'fields': ['doctor']}),
    ]
    list_display = ('__str__', 'doctor', 'tm', 'dt')
#    list_filter = ['dt', 'doctor']
#    search_fields = ['patient']


admin.site.register(IsIt)
admin.site.register(Doctor)
admin.site.register(Patient, PatientAdmin)
