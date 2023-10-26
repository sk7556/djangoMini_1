# AWS 연동 진행기록 

# 먼저 간단한 장고 블로그 만들기 
$ django-admin startproject tutorialdjango .
$ python3 manage.py migrate
$ python3 manage.py startapp blog
blog > models.py 수정
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ 
blog > Settings.py 
    MEDIA_ROOT = BASE_DIR / 'media'
    MEDIA_URL = '/media/'
    LANGUAGE_CODE = 'ko-kr'
    TIME_ZONE = 'Asia/Seoul'    
    'DIRS': [BASE_DIR / 'templates'], # templates
tutorialdjango > urls.py
blog > urls.py
templates > admin > base_site.html
blog > admin.py 
tutorlialdjango > urls.py
## 이상 모놀리식 기본 구성 



