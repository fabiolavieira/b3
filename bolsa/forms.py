from django import forms
from .models import Pregao, Ativos


class PregaoForm(forms.ModelForm):
    class Meta:
        model = Pregao
        fields = '__all__'


class AtivosForm(forms.ModelForm):
    class Meta:
        model = Ativos
        fields = ['quantidade']


# class AtivosForm(forms.Form):
#     acao = forms.ModelMultipleChoiceField(queryset=Pregao.objects.get(id))
#     quantidade = forms.IntegerField
