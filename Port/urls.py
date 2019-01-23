from django.urls import path
from .views import (home
)

app_name = 'Port'
urlpatterns = [
    path('', home, name ='home')
]