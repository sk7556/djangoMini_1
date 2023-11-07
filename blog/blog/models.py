from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    # 사용하게 되는 DB 릴레이션 
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    movieAd = models.TextField()
    thumb_image = models.ImageField(
        upload_to='blog/images/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    view_count = models.PositiveIntegerField(default=0)
    tags = models.ManyToManyField('Tag', blank=True) 

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
    
    def image_url(self):
        if self.thumb_image:
            return self.thumb_image.url
        
    @property
    def created_month(self):
        return self.created_at.strftime("%b")  # "1월"을 "Jan"으로 형식화

    @property
    def created_day(self):
        return self.created_at.strftime("%d")  # 일을 DD 형식으로 가져옴
    
    
class Comment(models.Model):
    # 댓글의 경우 다른 테이블로 관리 
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.message
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name
    
class movieComment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='movieComment'
    )
    movieAd = models.TextField()
    image = models.ImageField(
        upload_to='blog/images/movieSS/%Y/%m/%d/', blank=True)
    message = models.TextField()
    def __str__(self):
        return self.message