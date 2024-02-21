from pyexpat import model
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import date
from django.db.models.signals import pre_save




class Account(models.Model):
    username = models.CharField(("Tên đăng nhập"), max_length=50)
    password = models.CharField("Mật khẩu", max_length=50)
    fullname = models.CharField("Họ tên", max_length=100,blank=True)
    email = models.EmailField(("Email"), max_length=254,blank=True)

class Item(models.Model):
    _postInfo = (
        ('ND','Nhặt được'),
        ('TK','Tìm kiếm'),
    )
    _typeItem = (
        ('ID','Ví/Giấy tờ'),
        ('PET','Thú cưng'),
        ('PEOPLE','Người'),
        ('ED','Điện thoại/Tablet/Laptop'),
        ('KEY','Chìa khóa'),
        ('TRANSPORT','Xe máy/Ô tô'),
        ('OTHER','Đồ vật khác'),
    )
    title = models.CharField("Tiêu đề", max_length = 200, blank=True)
    content = models.CharField("Nội dung", max_length=200, blank=True, null=True )
    location = models.CharField("Địa điểm thất lạc đồ", max_length=200, blank=True, null=True)
    postInfo = models.CharField("Kiểu tin tức",max_length = 10,choices=_postInfo,blank=True, null=True, )
    typeItem = models.CharField("Loại đồ vật", max_length=10, choices=_typeItem,blank=True, null=True)
    image = models.ImageField("Ảnh đồ vật ( nếu có)",upload_to='images', blank=True, null=True , default=None)
    #Thông tin liên hệ của người nhặt được đồ
    email = models.EmailField("Email liên hệ", max_length=200,blank=True, null=True)
    phone = models.IntegerField("Số điện thoại liên hệ",  blank=True, null=True)
    date_time = models.DateTimeField("Thời gian đăng tin",blank=True, null=True)
    #Thông tin xác thực ai là người đăng tin
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='comments')
    content  = models.TextField()
    
    def __str__(self):
        return self.user.username

    
  

    
class Message(models.Model):
    _status = (
        ('W','Waiting'),
        ('S','Success'),
        ('F','Failed'),
    )
    sender = models.CharField(("Người gửi"), max_length=100)
    receiver = models.CharField(("Người nhận"), max_length=50)
    content = models.CharField(("Nội dung"), max_length=50)
    time = models.DateTimeField(("Thời gian"))
    status = models.CharField("Trạng thái tin nhắn",max_length=50,choices=_status,blank=True)
    
class menuItem(models.Model):
    nameItem = models.CharField("Tên kiểu đồ",max_length=50)
    amountLost = models.IntegerField(("Số lượng mất"))
    amountPick = models.IntegerField("Số lượng nhặt được")
    
class Profile(models.Model):
    user = models.OneToOneField(Account, null=True, on_delete = models.CASCADE)
    
    bio = models.TextField()
    
    def __str__(self):
        return (self.user) 
 



