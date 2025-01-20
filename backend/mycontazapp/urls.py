from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# Define a list of urls patterns
urlpatterns = [
  path('welcome', views.welcome, name='welcome'),
  path('about', views.about, name='aboutPage')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)