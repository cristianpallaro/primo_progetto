from django.shortcuts import render
def homepage(request):
    return render(request,"homepage.html")

def welcome(request):
    return render(request,"welcome.html")

def lista(request):
    return render(request,"lista.html")

def chi_siamo(request):
    return render(request,"chi_siamo.html")
# Create your views here.
def variabili(request):
    context={ 
    'var1':'prima v',
    'var2':'seconda v',
    'var3':'terza v'
    }
    return render(request,"variabili.html",context)