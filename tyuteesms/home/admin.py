from django.contrib import admin

# Register your models here.
from home.models import Actor
class ActorAdmin(admin.ModelAdmin):
    list_display=['id','name','gender']
admin.site.register(Actor,ActorAdmin)
