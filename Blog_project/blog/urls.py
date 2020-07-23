from django.contrib import admin
from django.urls import path, include
import blogapp.views
import recent.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name='home'),
    path('news_blog/<int:blog_id>', blogapp.views.detail, name="detail"),
    path('news_blog/new', blogapp.views.new, name='new'),
    path('news_blog/create', blogapp.views.create, name='create'),
    path('recent/', recent.views.recent, name='recent'),
    path('account/', include('account.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
