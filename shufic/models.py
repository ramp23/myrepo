from django.db import models
from datetime import datetime


# Create your models here.
class Video(models.Model):
    Video_URL = models.TextField(default='')
    Video_title = models.CharField(max_length=200, default='')
    Video_o = models.TextField(default='')
    Video_like = models.IntegerField(default=0)

    # Video_data = models.DateTimeField(default=datetime.now(), blank=True)

    class Meta():
        db_table = "Video"

    def __str__(self):
        return self.Video_URL


class Comment(models.Model):
    class Meta():
        db_table = "Comment"

    comment_text = models.TextField(verbose_name="Комментарий")
    comment_video = models.ForeignKey(Video, True)

    def __str__(self):
        return self.comment_text
