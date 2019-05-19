import self as self
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Pregao, Ativos
from .forms import PregaoForm, AtivosForm


def home(request):
    return render(request, 'home.html')


def listar_pregao(request):
    data = {}
    data['pregao'] = Pregao.objects.all()
    return render(request, 'pregao.html', data)


@csrf_exempt
def criar_pregao(request):
    form = PregaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_pregao')

    return render(request, 'pregao-form.html', {'form': form})


@csrf_exempt
def excluir_pregao(request, id):
    pregao = Pregao.objects.get(id=id)

    if request.method == 'POST':
        pregao.delete()
        return redirect('listar_pregao')

    return render(request, 'pregao-excluir.html', {'pregao': pregao})


def listar_ativos(request):
    ativos = Ativos.objects.all()
    return render(request, 'meusativos.html', {'ativos': ativos})


@csrf_exempt
def criar_ativo(request, id):
    pregao = Pregao.objects.get(id=id)
    # form = CriarAtivosForm(request.POST)
    # form.acao = pregao.id

    if request.method == "POST":
        form = AtivosForm(request.POST)
        if form.is_valid():
            ativo = form.save(commit=False)
            ativo.acao = pregao.id
            ativo.save()
            return redirect('listar_ativos')
    else:
        form = AtivosForm()

    # if form.is_valid():
    #     form.save()
    #     return redirect('listar_ativos')

    return render(request, 'ativos-form.html', {'form': form})



@csrf_exempt
def comprar_ativo(request, id):
    meusativos = Ativos.objects.all()
    pregao = Pregao.objects.get(id=id)
    form = AtivosForm(request.POST)

    if request.method == 'POST':
        form = AtivosForm(request.POST)
        if form.is_valid():
            if pregao in meusativos:
                ativo = form.save(commit=False)
                meuativo = Ativos.objects.get(id=id)
                meuativo.quantidade += ativo.quantidade
                meuativo.acao.quantidade -= ativo.quantidade
                meuativo.save()
                ativo.save_m2m()
                return redirect('listar_ativos')
            else:
                return criar_ativo(request, id)

    return render(request, 'ativos-form.html', {'form': form})
