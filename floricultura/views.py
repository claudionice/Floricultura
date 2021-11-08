from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import generics, decorators 
from floricultura.serializers import FloriculturaSerializer
from floricultura.models import planta, vaso 

@decorators.api_view (['GET'])
def plantas (request):
    planta = Planta.objects.all ()
    serializers = PlantaSerializer (planta, many=True)
    return Response (serializers.data)


# Create your views here.
