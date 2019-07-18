
from django.urls import path
from core.views import home, result

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('result/', result, name='result'),
]

