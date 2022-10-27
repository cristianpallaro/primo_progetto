from django.shortcuts import render
import random 
# Create your views here.
def index(request):
    return render(request,"index3.html")

def maxmin(request):
    context={
        'var1':random.randit(0,10),
        'var2':random.randit(0,10),
        'var3':var1+var2,
    }
    return render(request,"maxmin.html",context)

def media(request):
    return render(request,"media.html")