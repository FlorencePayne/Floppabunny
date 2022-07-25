from django.urls import path
from floppa import views
app_name = 'floppa'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('about/commissions/', views.commissions, name='commissions'),
    path('gallery', views.gallery, name='gallery'),
    path('more_floppa/', views.more_floppa, name='more_floppa'),
    path('register/', views.register, name='register'),
    path('signin/', views.signin, name='signin'),

]