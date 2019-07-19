
from django.urls import path
from core.views import home, result, opinion

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('opinion/', opinion, name='opinion'),
    path('result/', result, name='result'),
]
