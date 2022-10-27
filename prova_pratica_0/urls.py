from django.urls import path
from prova_pratica_0.views import index,maxmin,media

app_name="prova_pratica_0"
urlpatterns=[
    path('',index,name='index'),
    path('maxmin/',maxmin,name='maxmin'),
    path('media/',media,name='media'),
]
