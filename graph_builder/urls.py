from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:char_rank>/',views.graph_build_from_rank, name = 'graph_build_from_rank'),
    path('<char>/',views.graph_build, name='graph_build'),

]