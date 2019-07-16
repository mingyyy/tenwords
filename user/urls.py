from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from user.views import logout_view, register

app_name = 'user'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='user/login.html'), name="login"),
    path('logout/', logout_view, name="logout"),
    path('register/', register, name='register'),
]