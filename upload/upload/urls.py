"""upload URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from newbook import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$',views.home,name="home"),
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^login/$', views.user_login, name="login1"),
    url(r'^logout/$', views.user_logout, name="logout1"),
url(r'^upload/$',views.upload,name="upload"),
url(r'^list/$',views.booklist,name="list"),
    url(r'delete_book/(?P<p>[0-9]+)',views.delete_book,name="delete_book"),
 url(r'view_book/(?P<p>[0-9]+)',views.view_book,name="view_book"),
url(r'edit_book/(?P<p>[0-9]+)',views.edit_book,name="edit_book"),
url(r'order_book/(?P<p>[0-9]+)',views.order_book,name="order_book"),

    url(r'^status/$', views.order_status, name="status"),
    url(r'^search/$', views.search, name="search"),
]


if(settings.DEBUG):
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)