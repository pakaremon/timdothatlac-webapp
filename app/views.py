from urllib.request import HTTPRedirectHandler
from .models import Item, Comment
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import CreateNewPost, CreateNewPostAdmin, CommentForm

import time
from django.http import JsonResponse
from django.contrib import messages

from django import template


# import pagination stuff
from django.core.paginator import Paginator

 

#delete news 
@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.user.username == item.manager.username or request.user.is_superuser:
        item.delete()
        messages.success(request, "you have deleted item successful!")
        return HttpResponseRedirect(reverse('apps:indexApp'))
    else:
        messages.error(request, "You're not authorize.")
        render(request, "app/index.html")

def posts(request):
    dictionary ={}
    dictionary["items"]=Item.objects.all()
    
    # Get start and end points
    start = int(request.GET.get("start") or 0)
    end = int(request.GET.get("end") or (start + 9))

    # Generate list of posts
    data = []
    # for i in range(start, end + 1):
        
    #     data.append(f"Post #{i}")
    
    for item in dictionary["items"]:
        
        data.append(item.id)

    # Artificially delay speed of response
    time.sleep(1)

    # Return list of posts
    return JsonResponse({
        "posts": data
    })
    


@login_required
def add_post(request):
     # if this is a POST request we need to process the form data
    if request.method == 'POST':
        if request.user.is_superuser:    
            # create a form instance and populate it with data from the request:
            form = CreateNewPostAdmin(request.POST)
        else:
              form = CreateNewPost(request.POST)
        # # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('apps:save_form_sucess'))
        else:
            return HttpResponseRedirect(reverse('apps:save_form_fail'))
   
    # if a GET (or any other method) we'll create a blank form
    else:
        if request.user.is_superuser:
            form = CreateNewPostAdmin()
        else:
            form = CreateNewPost()

    return render(request, 'app/post.html', {'form': form})

# detail  information of the item
def item(request, pk):
    post = get_object_or_404(Item, pk=pk)
    form = CommentForm()
    if request.method=='POST':
        form = CommentForm(request.POST, user=request.user, post=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'./{pk}')
        
 
    return render(request, "app/item.html", {
        "item": post,
        "form":form,
       
    })

#Xóa tin tức
# def delete_news(request, item_id):
#     item = Item.objects.get(pk=item_id)
#     if request.user == item.manager:
#         item.delete()
#         messages.success(request, "Event deleted!")
#         return  HttpResponseRedirect(reverse('apps:news'))
#     else:
#          messages.success(request, "You're unauthorized ! ")
#          return  HttpResponseRedirect(reverse('apps:news'))
    


# Create your views here.
@login_required
def index(request):
    
    #set up pagination
    p = Paginator(Item.objects.all().order_by('-date_time'), 5)
    page = request.GET.get('page')
    items = p.get_page(page)
    nums = "a" * items.paginator.num_pages
    return render(request,'app/index.html',{
        "item_list": Item.objects.all(),
        'items': items,
        'nums':nums,
        
    })




    
#save form status
def save_form_sucess(request):
    return render(request, 'app/save_form_sucess.html')

def save_form_fail(request):
    return render(request, 'app/save_form_fail.html')
        
    
def introduce(request):
    return render(request,"app/introduce.html")
def terms(request):
    return render(request,"app/terms.html")
def policy(request):
    return render(request,"app/policy.html")
def donate(request):
    return render(request,"app/payment_page.html")
def donate_complete(request):
    return render(request, "app/donate_complete.html")
def warning(request):
    return render(request,"app/warning.html")
def report(request):
    return render(request,"app/reportError.html")
def search(request):
    return render(request,"app/searchAdvance.html")

# Hiển thị tất cả thông  tin mới nhất
def news(request):
    return render(request, "info/news.html", {
         "items": Item.objects.all().order_by('-date_time')
    })
#hiển thị nhặt được
def displaynew(request):
    return render(request, "info/news.html", {
        "items": Item.objects.filter(postInfo="ND").order_by('-date_time')
    })
#hiển thị tin tìm kiếm   
def  newsearch(request):
    return  render(request, "info/news.html", {
        "items": Item.objects.filter(postInfo="TK").order_by('-date_time')
    })
# hiển thi tin liên quan đến thú cưng

def searchpets(request):
    return render(request, "Info/news.html", {
        "items": Item.objects.filter(typeItem="PET").order_by('-date_time')
    })

# Hiện thị tin liên quan đến con người
def searchpeople(request):
    return render(request, "info/news.html", {
        "items": Item.objects.filter(typeItem="PEOPLE").order_by('-date_time')
    })

def search(request):
    return render(request, "app/searchAdvance.html")

def searchBar(request):
    if request.method == "POST":
        search = request.POST['searched']
        newitems = Item.objects.filter(title__contains=search)
        return render(request, "Info/searchbar.html",{
            'search': search,
            'newitems': newitems,
        })
    else:
        return render(request, "Info/searchbar.html")
