from django.contrib import admin
from django.urls import path, include
from .views import Main, CategoryList, AnegdotView, get_random_anegdot, Search

urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('category/<slug:slug>/', CategoryList.as_view(), name='category'),
    path('anegdot/<int:pk>/', AnegdotView.as_view(), name='anegdot'),
    path('search/', Search.as_view(), name='search'),
    path('random_anegdot/', get_random_anegdot, name='random'),
]
