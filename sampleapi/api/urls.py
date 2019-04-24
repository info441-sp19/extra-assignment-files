from . import views
from django.urls import path

app_name = 'api'
urlpatterns = [
        path('makedog', views.makeDog, name='makeDog'),
]
