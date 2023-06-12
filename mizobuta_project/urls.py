from django.contrib import admin
from django.urls import path
from mizobuta.views import index,main_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('main-page/', main_page, name='main_page'),
]
