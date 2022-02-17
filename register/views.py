from django.shortcuts import render, redirect
from .models import Livro

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    if request.method == 'POST':
        nome = request.POST.get('nome')
        editora = request.POST.get('editora')
        sinopse = request.POST.get('sinopse')
        ano = request.POST.get('ano')

        if len(nome.strip()) == 0:
            return render(request, 'register.html', {"response": "Não deixe o nome do livro em branco."})

        try:
            livro = Livro(nome = nome, editora = editora, sinopse = sinopse, ano = ano)
            livro.save()

            return render(request, 'register.html', {"response": "Livro cadastrado com sucesso!"})

        except:

            return render(request, 'register.html', {"response": "Falha em cadastrar o livro."})