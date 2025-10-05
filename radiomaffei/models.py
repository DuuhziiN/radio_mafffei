from django.db import models

class Music(models.Model):
    titulo = models.CharField(max_length=100)
    arquivo = models.FileField(upload_to='musicas/')
    class Meta:
        # Permissão para restringir o acesso à página do radialista
        permissions = [
            ("can_access_radialista", "Pode acessar o painel do radialista e transmitir"),
        ]
    def __str__(self):
        return self.titulo

from django.db import models

class Musica(models.Model):
    # O campo FileField é crucial para lidar com uploads de arquivos.
    arquivo = models.FileField(upload_to='musicas/')
    titulo = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        # Retorna o nome do arquivo ou o título para melhor visualização no Admin
        return self.titulo if self.titulo else self.arquivo.name