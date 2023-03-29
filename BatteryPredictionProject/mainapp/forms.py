from dataclasses import fields
from django.forms import ModelForm
from .models import UserPrediction

class UserPredictionForm(ModelForm):
    class Meta:
        model = UserPrediction
        fields = '__all__'
        exclude = ['prediction_id','timestamp']