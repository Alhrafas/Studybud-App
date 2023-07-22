from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view('GET')
def getRoutes(request):
      routes = [
            'GET /ap1',
            'GET /api/rooms',
            'GET /api/rooms/:id'
      ]
      return JsonResponse(routes, safe=False)