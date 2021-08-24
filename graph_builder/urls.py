from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name = "dashboard"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name = 'register'),

    path('', views.index, name='index'),
    path('<int:char_rank>/',views.graph_build_from_rank, name = 'graph_build_from_rank'),
    path('<char>/', views.graph_build, name='graph_build'),
]