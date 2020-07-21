from django.contrib import admin
from django.urls import path
import myapp.views.py


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.index, name="index"),
]
