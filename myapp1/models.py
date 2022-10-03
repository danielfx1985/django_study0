from django.db import models

# Create your models here.
from django.db import models





class wenzhang(models.Model):
    def __str__(self):
        return self.content
   # news_id=models.IntegerField(default=0)
    title=models.CharField(max_length=500)
    content=models.CharField(max_length=1500)
    #pubdate=models.DateTimeField('date published')
    parent_id=models.IntegerField(default=0)
    wenzhang_type=models.CharField(max_length=50)


