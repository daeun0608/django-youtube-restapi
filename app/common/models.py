from django.db import models

class CommonModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True # db에 추가하지않고 상속으로 활용
