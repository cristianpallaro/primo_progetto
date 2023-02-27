
from django.contrib import admin
from django.urls import path,include
from .views import index_generale


urlpatterns = [
    path('admin/', admin.site.urls),
    path('prima_app/',include('prima_app.urls',namespace="prima_app")),
    path('seconda_app/',include('seconda_app.urls',namespace="seconda_app")),
    path('',index_generale, name="index_generale"),
    path('prova_pratica_0/',include('prova_pratica_0.urls',namespace="prova_pratica_0")),
    path('prova_pratica_1/',include('prova_pratica_1.urls',namespace="prova_pratica_1")),
    path('news_app/',include('news_app.urls',namespace="news_app")),

    
]
#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]