from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('new_post/', views.new_post, name='new_post'),
    path('<slug:slug>', views.post_details, name='post_details'),
    path('delete_blog_post/<slug:slug>/', views.delete_post,name='delete_blog_post'),
    path('update_blog_post/<slug:slug>/', views.update_post,name='update_blog_post'),
]
