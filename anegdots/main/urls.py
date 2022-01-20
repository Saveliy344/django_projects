from django.contrib import admin
from django.urls import path, include
from .views import Main, CategoryList, AnegdotView, get_random_anegdot, register, user_login, user_logout, send_message
from django.views.decorators import cache

urlpatterns = [
    # path('', cache.cache_page(60)(Main.as_view()), name='main'),
    # path('category/<slug:slug>/', cache.cache_page(60)(CategoryList.as_view()), name='category'),
    path('', Main.as_view(), name='main'),
    path('category/<slug:slug>/', CategoryList.as_view(), name='category'),
    path('anegdot/<int:pk>/', AnegdotView.as_view(), name='anegdot'),
    path('random_anegdot/', get_random_anegdot, name='random'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('feedback/', send_message, name='FeedBack'),
]
