from django.contrib import admin
from . import models

# Register your models here.

class TweetAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Message Group', {"fields": ["meessage"]}),
        ('Nickname Group', {"fields": ["nickname"]})
    ]
    #fields = ["message","nickname",]


admin.site.register(models.Tweet, TweetAdmin)

