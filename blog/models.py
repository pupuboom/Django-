from django.db import models

# Create your models here.
class Article(models.Model):
    #文章id
    articleId=models.AutoField(primary_key=True)
    #文章标题
    title=models.TextField()
    #文章摘要
    abstract=models.TextField()
    #文章内容
    content=models.TextField()
    #发布日期
    publishData=models.DateField(auto_now=True)
    def __str__(self):
        return self.title