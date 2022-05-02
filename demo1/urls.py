from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
from . import views

# Create your urls here.
app_name = 'demo1'
urlpatterns = [
    path('', views.index, name='index'),
    path('invites/', views.invite, name='invite'),
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
