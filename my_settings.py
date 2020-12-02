# https://velog.io/@devmin/Django-MySQL-Connect
# my_settings.py: 깃헙과 같은 곳에 공유하면 안되는 정보들을 저장해서 사용. 
# 깃헙에 올릴 때는 이 파일을 .gitignore에 넣어야한다.
DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',    
        'NAME': 'amator',                  
<<<<<<< HEAD
        'USER': 'root',
        'PASSWORD': 'samsung1',
=======
        'USER': 'root',                          
        'PASSWORD': '2017152013',                  
>>>>>>> 21d563a955e287f2e616c28d27bd25289aa32b71
        'HOST': 'localhost',                     
        'PORT': '3306',                          
    }
}