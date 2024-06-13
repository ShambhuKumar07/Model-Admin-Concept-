from django.contrib import admin
from enroll.models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display=("std_id","std_name","std_email","std_pass")


admin.site.register(Student,StudentAdmin)