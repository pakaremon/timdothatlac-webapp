from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
app_name = "apps"
#name space
urlpatterns = [
    path('',views.index,name='indexApp'),
    path('add/', views.add_post, name='postnew'),
    path('sucess/', views.save_form_sucess, name='save_form_sucess'),
    path('fail/', views.save_form_fail, name='save_form_fail'),
    path("<int:pk>", views.item, name="item"),
    path('<int:pk>', views.delete, name='delete'),# delete new post
    path('policy/',views.policy,name="policy"),
    path('warning/', views.warning, name="warning"),
    path('donate/', views.donate, name="donate"),
    path('donate-complete/', views.donate_complete, name='donate-completed'),
    path('terms/', views.terms, name="terms"),
    path('introduce/', views.introduce, name="introduce"),
    path('report/',views.report,name="reportError"),
    path("search/",views.search, name="searchAdvance"),
    path("display_new/", views.displaynew, name="displaynew"),
    path("new-search/", views.newsearch, name="new-search"),
    path("new-pets/", views.searchpets, name="search-pets"),
    path("new-people/", views.searchpeople, name="search-people"),
    path("news/", views.news, name="news"),
    path("posts", views.posts, name="posts"),
    path("searchbar/", views.searchBar, name='search-bar'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)