from rest_framework import serializers
from floricultura.models import Planta, Vaso

class PlantaSerializers (serializers.ModelSerializer):
    class Meta ():
        model= Planta
        fields = '__all__'

class VasoSerializers (serializers.ModelSerializer):
    class Meta ():
        model= Vaso 
        fields = '__all__'