from django.shortcuts import render, get_object_or_404
from .models import Recent

# Create your views here.


def recent(request):
    recents = Recent.objects
    return render(request, 'recent.html', {'recents': recents})
