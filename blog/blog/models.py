from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import os

def custom_image_path(instance, filename):
    # 현재 날짜 및 시간 가져오기
    now = datetime.now()
    # 폴더 경로를 연월일 형식으로 만들기
    folder_path = now.strftime('blog/images/%Y/%m/%d/')
    # 파일명에 현재 날짜와 시간 정보 추가
    new_filename = now.strftime('%Y%m%d%H%M%S') + os.path.splitext(filename)[1]
    # 최종 파일 경로 반환
    return os.path.join(folder_path, new_filename)

class Post(models.Model):
    # 사용하게 되는 DB 릴레이션 
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    movieAd = models.TextField()
    thumb_image = models.ImageField(
        upload_to=custom_image_path, blank=True)
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
    class Meta:
        ordering = ['-created_at']
    
        
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