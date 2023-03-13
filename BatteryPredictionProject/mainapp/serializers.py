from rest_framework import serializers

class PredictionAPISerializer(serializers.Serializer):
    """ Serializer for prediction API """

    capacity = serializers.FloatField()
    voltage_measured = serializers.FloatField()
    current_measured = serializers.FloatField()
    temperature_measured = serializers.FloatField()
    current_load = serializers.FloatField()
    voltage_load = serializers.FloatField()
    time = serializers.IntegerField()