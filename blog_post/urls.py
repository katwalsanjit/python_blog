
from django.urls import path
# from .import views (.) dot means same directory
#import views
# this is taken from root this is also called absolute or static method
from blog_post import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("", views.test_home, name="test_home")
]
