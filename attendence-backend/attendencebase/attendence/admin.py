from django.contrib import admin

# Register your models here.
from attendence.models import Attendence, Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ()
    search_fields = ()

admin.site.register(Student, StudentAdmin)

class AttendenceAdmin(admin.ModelAdmin):
    list_display = ()
    search_fields = ()

admin.site.register(Attendence, AttendenceAdmin)