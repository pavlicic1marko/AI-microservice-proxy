from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def getRoutes(request):
    routes= ['api/products','api/products/<id>']
    return Response(routes)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProducts(request):
    return Response({'test-key':'test123'})
