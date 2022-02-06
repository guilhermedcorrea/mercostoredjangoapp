from django.shortcuts import render, get_object_or_404, redirect
from .models import Seller, Produtos, User, CategoriasProdutos, Googleshopping
from django.http import Http404
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages


# Create your views here.
def index(request):
    try:
        contatos = Produtos.objects.all()
        paginator = Paginator(contatos, 3)
        page = request.GET.get('p')
        contatos = paginator.get_page(page)

        return render(request, 'sellers/index.html',{
            'contatos':contatos
        })
    except Produtos.DoesNotExist as e:
        raise Http404()


def ver_contato(request, contato_id):
    try:
        contato = Produtos.objects.get(id=contato_id)
        #contato = get_object_or_404(Contato, contato_id)
        return render(request, 'sellers/ver_contato.html', {
            'contato':contato
        })
    except Produtos.DoesNotExist as e:
        raise Http404()


def busca(request):
    termo = request.GET.get('termo')

    if termo is None or not termo:
        messages.add_message(
            request,
            messages.ERROR,
            'Campo termo não pode ficar vazio.'
        )
        return redirect('index')

    campos = Concat('nome', Value(' '), 'sobrenome')

    contatos = Produtos.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo)
    )

    paginator = Paginator(contatos, 20)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'sellers/busca.html', {
        'contatos': contatos
    })
