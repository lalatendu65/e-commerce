from django.contrib import admin

# Register your models here.
from lpj.models import *
class studentAdmin(admin.ModelAdmin):
    list_display=['id','name']
admin.site.register(student,studentAdmin)

admin.site.register(product)

