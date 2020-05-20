from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})

class Comment(models.Model):
    sno=models.AutoField(primary_key=True)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    message=models.TextField()
    post_id=models.ForeignKey(Post,on_delete=models.CASCADE)
    date_time=models.DateTimeField(default=timezone.now)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)

