from rest_framework import viewsets
from floricultura.models import Planta, Vaso
from floricultura.serializers import PlantaSerializers, VasoSerializers

class PlantaViewSets (viewsets.ModelViewSet):
    queryset = Planta.objects.all ()
    serializers_class = PlantaSerializers 

class VasoViewSets (viewsets.ModelViewSet):
    queryset = Vaso.objects.all ()
    serializers_class = VasoSerializers 

# Create your views here.
