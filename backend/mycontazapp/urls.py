from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# Define a list of urls patterns
urlpatterns = [
  path('contacts', views.ContactView.as_view(), name='contact'),
  path('contacts/<id>', views.SingleContactView.as_view(), name='single-contact')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)