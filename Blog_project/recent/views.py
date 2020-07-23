from django.shortcuts import render


# Create your views here.


def recent(request):
    return render(request, 'recent.html')
