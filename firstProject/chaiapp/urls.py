# filepath: d:\Chai aur Django\firstProject\chaiapp\urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_chai, name="all_chai"),
    path('chai/', views.all_chai, name="all_chai"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)