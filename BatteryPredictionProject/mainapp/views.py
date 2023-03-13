from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .LSTM import prediction

from . import serializers

from django.shortcuts import render





class predictionsapi(APIView):
    # """Test API View"""
    predictionserializer = serializers.PredictionAPISerializer
    #This is just a test GET method
    def get(self, request, format=None):
        """ Get predictions """
        an_apiview = ['Enjoy the API!', 'Try it out!']

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    #TEST

    def post(self, request):
        """ Create a predictions API(based on data pass from user) """
        serializer = self.predictionserializer(data=request.data)
        if serializer.is_valid():
            capacity = serializer.validated_data.get('capacity')
            voltage_measured = serializer.validated_data.get('voltage_measured')
            current_measured = serializer.validated_data.get('current_measured')
            temperature_measured = serializer.validated_data.get('temperature_measured')
            current_load = serializer.validated_data.get('current_load')
            voltage_load = serializer.validated_data.get('voltage_load')
            time = serializer.validated_data.get('time')

            prediction_result = prediction([[capacity, voltage_measured, current_measured, temperature_measured, current_load, voltage_load, time]])
            
            # return the result as the response
            return Response({'prediction': prediction_result})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)