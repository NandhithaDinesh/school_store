from django.contrib import admin

# Register your models here.
from . models import  Department,Material, Course,FormEntry
admin.site.register(Department),
admin.site.register(Material),
admin.site.register(Course),
admin.site.register(FormEntry),
