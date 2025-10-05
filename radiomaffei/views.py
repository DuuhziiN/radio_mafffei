# Arquivo: radiomaffei/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .forms import MusicaForm
from .models import Musica 

# =========================================================
# 1. VIEW DA PÁGINA DO OUVINTE (PÚBLICA)
# =========================================================
def pagina_ouvinte(request):
    musicas = Musica.objects.all().order_by('-id') 
    context = {'musicas': musicas}
    return render(request, 'home.html', context)

# =========================================================
# 2. VIEW DO PAINEL DO RADIALISTA (RESTRITA)
# =========================================================
# Restringe o acesso apenas a quem tem a permissão 'can_access_radialista'
@permission_required('radiomaffei.can_access_radialista', login_url='/contas/login/')
def pagina_radialista(request):
    
    form = MusicaForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('radiomaffei:radialista') 

    musicas = Musica.objects.all().order_by('-id')
    
    context = {
        'musicas': musicas,
        'form': form 
    }
    return render(request, 'radialista.html', context)


# =========================================================
# 3. VIEW PARA DELETAR MÚSICA
# =========================================================
@permission_required('radiomaffei.can_access_radialista', login_url='/contas/login/') 
def deletar_musica(request, musica_id):
    musica = get_object_or_404(Musica, pk=musica_id)
    
    if request.method == 'POST':
        musica.arquivo.delete() 
        musica.delete() 
        
        return redirect('radiomaffei:radialista')
        
    return redirect('radiomaffei:radialista')