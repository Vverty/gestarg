from django.urls import path
from Users import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login_request, name='Login'),
    path('', views.index_users, name='InicioUsers'),
    path('register/', views.register, name='Register'),
    path('nosotros/', views.nosotros, name='Nosotros'),
    path('logout/', LogoutView.as_view(template_name='Users/index_users.html'), name="Logout")
]