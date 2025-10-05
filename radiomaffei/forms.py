from django import forms
from .models import Music

from django import forms
from .models import Musica

class MusicaForm(forms.ModelForm):
    class Meta:
        model = Musica
        # Incluímos o campo 'arquivo' para o upload. 'titulo' é opcional.
        fields = ('titulo', 'arquivo',)