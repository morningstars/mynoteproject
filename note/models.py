from django.db import models


# Create your models here.
from django.db.models import CASCADE

from user.models import User

class Note(models.Model):
    title = models.CharField('标题', max_length=50)
    content = models.CharField('内容', max_length=300)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    mod_time = models.DateTimeField('修改时间', auto_now=True)
    user = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return "标题：" + self.title + "内容：" + self.content
