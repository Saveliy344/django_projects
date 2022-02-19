from django.urls import path
import main.views as views

urlpatterns = [
    path('', views.Main.as_view(), name='main'),
    path('categories/<slug:slug>', views.Categories.as_view(), name='categories'),
    path('product/<slug:slug>', views.get_product, name='product'),
    path('feedback/', views.feedback, name='feedback'),
    path('cart/', views.get_cart, name='cart'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('logout/', views.make_logout, name='logout'),
    path('order/', views.make_order, name='order'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('register/', views.RegisterUser.as_view(), name='register'),
]
