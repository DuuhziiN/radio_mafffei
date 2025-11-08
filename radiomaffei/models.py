# Arquivo: radiomaffei/models.py (VERSÃO SIMPLES)

from django.db import models

class Musica(models.Model):
    # Removendo 'storage=OverwriteStorage()' para usar o padrão
    arquivo = models.FileField(
        upload_to='musicas/',
    )
    titulo = models.CharField(max_length=100, blank=True, null=True)
    
    class Meta:
        permissions = [
            ("can_access_radialista", "Pode acessar o painel do radialista e transmitir"),
        ]

    def __str__(self):
        return self.titulo if self.titulo else self.arquivo.name