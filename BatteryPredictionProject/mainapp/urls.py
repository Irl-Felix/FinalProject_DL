
from django.urls import path,include
from . import views


urlpatterns = [
    #Show EVERYTHING(ADMIN VIEW)
    path('dashboard/', views.dashboard,name='dashboard'),
    #PREDICTION INPUT
    path('userprediction/', views.make_predictions,name='userprediction'),
    path('profileSetting/', views.Profilesettings,name='profile_settings'),
]
