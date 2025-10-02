from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,"core/home.html")

def quienessomos(request):
    return render(request,"core/quienessomos.html")



def suscribete(request):
    return render(request,"core/suscribete.html")


