from django.urls import path
from myapp import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('search/', views.search, name='search'),
    path('get_image/', views.get_image, name='image'),
    path('show/', views.show_image, name='show_image'),
]

