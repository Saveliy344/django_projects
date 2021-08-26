from django.views.decorators.cache import cache_page
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', cache_page(60)(Home.as_view()), name='home'),
    path('about/', about, name='about'),
    path('addpage/', Addpage.as_view(), name='addpage'),
    path('contact/', FeedBack.as_view(), name='contact'),
    path('category/<slug:slug_name>/', ShowCategory.as_view(), name='category'),
    path('show_post/<slug:slug_name>/', ShowPost.as_view(), name='showpost'),
    path('update_post/<slug:slug_name>/', UpdatePost.as_view(), name='update'),
    path('del_post/<slug:slug_name>/', DeletePost.as_view(), name='delete'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]
