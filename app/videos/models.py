from django.db import models
from common.models import CommonModel

class Video(CommonModel):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    link = models.URLField()
    category = models.CharField(max_length=20)
    views_count = models.PositiveIntegerField(default=0)
    thumbnail = models.URLField()
    video_file: models.FileField(upload_to='storage/')

    user=models.ForeignKey('users.User', on_delete=models.CASCADE) # 유저 삭제 시 영상도 삭제
