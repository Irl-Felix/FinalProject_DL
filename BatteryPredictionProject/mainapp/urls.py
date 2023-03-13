
from django.urls import path,include
from . import views


urlpatterns = [
    path('predictions/', views.predictionsapi.as_view(), name='predictionsapi'),
]