from rest_framework import viewsets
from floricultura.models import Planta, Vaso
from floricultura.serializers import PlantaSerializers, VasoSerializers



class PlantaViewSets (viewsets.ModelViewSet):
    queryset = Planta.objects.all ()
    serializer_class = PlantaSerializer (planta, many=True)

class VasoViewSets (viewsets.ModelViewSet):
    queryset = Vaso.objects.all ()
    serializers_class = VasoSerializers (vaso, many=True)

# Create your views here.
