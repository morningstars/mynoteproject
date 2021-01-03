from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField('用户名', max_length=30)
    password = models.CharField('密码', max_length=30)

    def __str__(self):
        return "用户名：" + self.username


class Note(models.Model):
    title = models.CharField('标题', max_length=50)
    content = models.CharField('内容', max_length=300)
    create_time = models.DateField('创建时间')
    mod_time = models.DateField('修改时间')
    user = models.ForeignKey(User)

    def __str__(self):
        return "标题：" + self.title + "内容：" + self.content
