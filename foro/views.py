from django.shortcuts import render

from .models import Noticia
from django.core.paginator import Paginator 



# Create your views here.
#def noticias(request):
#    noticia=Noticia.objects.all() # lista de noticias
#    return render(request,'foro/noticias.html',
#                  {'noticia':noticia})



def noticias(request):
    lista_noticias = Noticia.objects.all().order_by('-created')  # opcional: ordena por fecha
    paginator = Paginator(lista_noticias, 5)  # 5 noticias por página
    page_number = request.GET.get('page')    # número de página desde la URL
    page_obj = paginator.get_page(page_number)
    return render(request, 'foro/noticias.html', {'page_obj': page_obj})
