from django.contrib import admin
from .models import UserProfile,Trip,UserPrediction,UserPredictionResult



admin.site.register(UserProfile)
admin.site.register(Trip)
admin.site.register(UserPrediction)
admin.site.register(UserPredictionResult)
