from django.contrib import admin
from django.urls import path
import mapapp.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mapapp.views.index),
]
