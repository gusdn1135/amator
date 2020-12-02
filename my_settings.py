# https://velog.io/@devmin/Django-MySQL-Connect
# my_settings.py: 깃헙과 같은 곳에 공유하면 안되는 정보들을 저장해서 사용. 
# 깃헙에 올릴 때는 이 파일을 .gitignore에 넣어야한다.
DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',    
        'NAME': 'amator',                  
        'USER': 'root',                          
<<<<<<< HEAD
        'PASSWORD': 'samsung1',                  
=======
        'PASSWORD': '2017152013',                  
>>>>>>> 4a6f494961f4d70e8f69c8c41409e1997dde8121
        'HOST': 'localhost',                     
        'PORT': '3306',                          
    }
}