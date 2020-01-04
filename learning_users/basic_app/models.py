from django.db import models
# Creating a user model
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
    '''
    OneToOneField 我們最常用的時機就是擴充 ( extends )
    Django 的 User Model 預設已經有一些存在的 field ，但很多時候我們常常需要增加一些額外的資料，像是需要記錄使用者的生日，這時候OneToOneField 就派上用場了。建立一個 UserProfileInfo 的 model，透過OneToOneField 和 User Model 建立 一對一 （ one-to-one ） 的關係。
    '''
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    # additional classes
    # blank = True means users do not have to fill the field
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to = 'profile_pics', blank=True)

    def __str__(self):
        return self.user.username
        # username is a default attribute of User
        # 因為有把User繼承，因此可以呼叫。(user = models.OneToOneField(User))
    '''
    如果要讓image起作用，必須要先安裝pillow:
    在命令提示字元打上 pip install pillow
    '''
