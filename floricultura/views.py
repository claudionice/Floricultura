from rest_framework.response import Response
from rest_framework import generics, decorators 
from serializers import PlantaSerializer 
from floricultura.models import Planta, Vaso


@decorators.api_view (['GET',])
def planta (request):
    planta = Planta.objects.all ()
    serializers = PlantaSerializer (planta, many=True)
    return Response (serializers.data)


# Create your views here.
