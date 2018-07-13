from django.contrib import admin
from shufic.models import Video
from shufic.models import Comment


class VideoInLine(admin.StackedInline):
    model = Comment
    extra = 2

class VideoAdmin(admin.ModelAdmin):
    inlines = [VideoInLine]

# Register your models here.
admin.site.register(Video, VideoAdmin)