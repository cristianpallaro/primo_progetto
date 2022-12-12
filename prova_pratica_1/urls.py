from django.urls import path
from prova_pratica_1.views import view_a,view_b,view_c,index3
app_name="seconda_app"
urlpatterns=[
    path("view_a/",view_a,name="view_a"),
    path("view_b/",view_b,name="view_b"),
    path("view_c/",view_c,name="view_c"),
   # path('index3/',index3,name='index3'),
]