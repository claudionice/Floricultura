from rest_framework import viewset
from floricultura.models import Planta, Vaso
from serializer import PlantaSerializer, VasoSerializer



class PlantaViewSet (viewset.ModelViewSet):
    queryset = Planta.objects.all ()
    serializer_class = PlantaSerializer (planta, many=True)

class VasoViewSet (viewset.ModelViewSet):
    queryset = Vaso.objects.all ()
    serializer_class = VasoSerializer (vaso, many=True)

# Create your views here.
