
# from django.contrib import admin
from django.urls import path  # include
from django.conf.urls import include, url
from db import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^$', views.home, name='index'),
    path('login', views.login, name='login'),
    url(r'^', include('db.urls')),
]

handler404 = views.handler404

# handler500 = 'views.handler500'
