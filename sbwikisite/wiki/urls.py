from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('class/<str:game_class>/', views.gameClass, name='gameClass'),
    path('media/<str:name>', views.MediaQuery, name='mediaQuery'),
    path('discipline/<str:disc>/', views.DisciplineView, name='DisciplineView'),
    path('race/<str:race>/', views.RaceView, name='RaceView'),
    path('base-class/<str:base>/', views.BaseClassView, name='BaseClassView'),
]