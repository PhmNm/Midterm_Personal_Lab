from django.urls import path
from . import views
urlpatterns = [
    path('register', views.registerPage, name='register'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),

    path('',views.home, name="home"),
    path('products/',views.products, name="products"),
    path('customer/<str:id>/',views.customer, name="customer"),
    path('create_order/<str:id>', views.createOrder, name='create_order'),
    path('update_order/<str:id>/', views.updateOrder, name='update_order'),
    path('delete_order/<str:id>/', views.deleteOrder, name='delete_order')
]