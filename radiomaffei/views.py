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
        # Remove o arquivo físico (no Render, ele é temporário)
        musica.arquivo.delete() 
        musica.delete() 
        
        return redirect('radiomaffei:radialista')
        
    return redirect('radiomaffei:radialista')

def programacao(request):
    # Esta view pode ser usada para passar dados de programação no futuro
    return render(request, 'programacao.html')

def sobre_nos(request):
    return render(request, 'sobre_nos.html')

def equipe(request):
    # Dados de exemplo para a equipe
    equipe_membros = [
        {'nome': 'Alicya', 'foto': 'img/equipe/Alicya.jpg'},
        {'nome': 'Emanuelly', 'foto': 'img/equipe/Emanuelly.jpg'},
        {'nome': 'Italo', 'foto': 'img/equipe/Italo.jpg'},
        {'nome': 'Luiz B.', 'foto': 'img/equipe/LuizB.jpg'},
        {'nome': 'Marla', 'foto': 'img/equipe/Marla.jpg'},
        {'nome': 'Nicolly', 'foto': 'img/equipe/nicolly.jpg'},
    ]
    return render(request, 'equipe.html', {'membros': equipe_membros})

def midias(request):
    # Lista de URLs de imagens/mídia de exemplo para a página
    galeria_midia = [
        'img/midia/evento1.jpeg', 'img/midia/evento2.jpeg', 'img/midia/evento3.jpeg',
        'img/midia/evento4.jpeg', 'img/midia/evento5.jpeg', 
    ]
    return render(request, 'midias.html', {'galeria': galeria_midia})

def concursos_programas(request):
    return render(request, 'concursos_programas.html')