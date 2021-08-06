from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<txt>',views.graph_build, name='graph_build')
]