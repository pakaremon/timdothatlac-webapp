from django import forms
from django.forms import ModelForm
from .models import Item, Comment
import re
import datetime


#Comment form
class CommentForm(ModelForm):
    def __init__(self, *args, **kwargs ):
        self.user = kwargs.pop('user', None)
        self.post = kwargs.pop('post', None)
        super().__init__(*args, **kwargs)
    
    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.user = self.user
        comment.post = self.post
        comment.save()
         
    
    # date = forms.DateTimeField(initial=datetime.datetime.now()
    class Meta:
        
        model = Comment
        fields = ["content"]
        
        widgets = {
            'content': forms.TextInput(attrs={'class': 'form-control'})
        }
          
    
    
#admin post new form
class CreateNewPostAdmin(ModelForm):
    
    postInfo = (
        ('ND','Nhặt được'),
        ('TK','Tìm kiếm'),
    )
    
    typeItem = (
        ('ID','Ví/Giấy tờ'),
        ('PET','Thú cưng'),
        ('PEOPLE','Người'),
        ('ED','Điện thoại/Tablet/Laptop'),
        ('KEY','Chìa khóa'),
        ('TRANSPORT','Xe máy/Ô tô'),
        ('OTHER','Đồ vật khác'),
    )
   
    postInfo = forms.ChoiceField(help_text='Kiểu tin tức',choices=postInfo,)
    typeItem = forms.ChoiceField(help_text="Loại đồ vật",choices=typeItem,)
    date_time = forms.DateTimeField(initial=datetime.datetime.now())
   

    class Meta:
        model = Item
        fields = ('title','content','manager','location','postInfo','typeItem','image','email','phone','date_time',)
        

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id':'title_form', }),
            'content': forms.TextInput(attrs={'class': 'form-control', }),
            'manager': forms.Select(attrs={'class': 'form-select', 'placeholder':'User',}),
            'location': forms.TextInput(attrs={'class': 'form-control', }),
            'email': forms.TextInput(attrs={'class': 'form-control', }),
            'phone': forms.TextInput(attrs={'class': 'form-control', }),
            

        }



#user post new form
class CreateNewPost(ModelForm):
    
    postInfo = (
        ('ND','Nhặt được'),
        ('TK','Tìm kiếm'),
    )
    typeItem = (
        ('ID','Ví/Giấy tờ'),
        ('PET','Thú cưng'),
        ('PEOPLE','Người'),
        ('ED','Điện thoại/Tablet/Laptop'),
        ('KEY','Chìa khóa'),
        ('TRANSPORT','Xe máy/Ô tô'),
        ('OTHER','Đồ vật khác'),
    )
   
    postInfo = forms.ChoiceField(help_text='Kiểu tin tức',choices=postInfo,)
    typeItem = forms.ChoiceField(help_text="Loại đồ vật",choices=typeItem,)
    date_time = forms.DateTimeField(initial=datetime.datetime.now())
   

    class Meta:
        model = Item
        fields = ('title','content','location','postInfo','typeItem','image','email','phone','date_time',)
        

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id':'title_form', }),
            'content': forms.TextInput(attrs={'class': 'form-control', }),
            'location': forms.TextInput(attrs={'class': 'form-control', }),
            'email': forms.TextInput(attrs={'class': 'form-control', }),
            'phone': forms.TextInput(attrs={'class': 'form-control', }),
            

        }



