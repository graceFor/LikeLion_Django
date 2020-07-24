from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def kakao(request):
    return render(request, 'kakao.html')
