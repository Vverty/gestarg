from django.urls import path
from Users import views

urlpatterns = [
    path('login/', views.login_request, Name='Login'),
    path('register/', views.register, Name='Register')
]