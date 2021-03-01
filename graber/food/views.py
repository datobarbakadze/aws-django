from django.shortcuts import render


def index(request):
    resposne = {'insert_me': 'hahahaha'}
    return render(request, 'food/index.html', context=resposne)


def detail(request):
    resposne = {'details': 'I am detail page'}
    return render(request, 'food/detail.html', context=resposne)
