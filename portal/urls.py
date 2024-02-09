from django.urls import path

from portal import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.CustomerCreateView.as_view(), name='register'),
    path('update/<int:pk>/', views.CustomerUpdateView.as_view(), name='update'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
]
