import email
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True,blank=True ,on_delete=models.CASCADE,related_name='user_profile')
    gender = models.CharField(max_length=10, blank=True)
    occupation = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    preferred_language = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=100, blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    car_brand = models.CharField(max_length=30)
    car_model = models.CharField(max_length=30)
    YEAR_CHOICES = [(year, year) for year in range(2010, 2024)]
    year_of_car = models.IntegerField(choices=YEAR_CHOICES, null=True, blank=True)
    battery_of_car = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.first_name}'


#
class Trip(models.Model):
    trip_id = models.AutoField(primary_key=True)
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='trips')
    origin = models. CharField(max_length=100)
    destination = models.CharField(max_length=100)
    distance_meters = models.FloatField()
    duration_sec = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.trip_id}--({self.timestamp.strftime('%Y-%m-%d %H:%M:%S')})"


class UserPrediction(models.Model):
    prediction_id = models.AutoField(primary_key=True)
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='predictions')
    capacity = models.FloatField()
    voltage_measured = models.FloatField()
    current_measured = models.FloatField()
    temperature_measured = models.FloatField()
    current_load = models.FloatField()
    voltage_load = models.FloatField()
    time_duration = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.userprofile.first_name}--({self.timestamp.strftime('%Y-%m-%d %H:%M:%S')})"

class UserPredictionResult(models.Model):
    result_id = models.AutoField(primary_key=True)
    entered_prediction = models.ForeignKey(UserPrediction, on_delete=models.CASCADE, related_name='prediction_results')
    predicted_value = models.FloatField()
    result_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.predicted_value}"