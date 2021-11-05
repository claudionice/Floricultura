from django.http import JsonResponse

def plantas (request):
    if request.method == 'GET':
        plantas = {'id': 1, 'nome': 'Tulipas'}
        return JsonResponse(plantas)


# Create your views here.
