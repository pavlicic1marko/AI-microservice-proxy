from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from AppAI.models import Prompt
from AppAI.serializer import PromptSerializer

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


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getPrompts():
    user_id = 1
    promts_for_user = Prompt.objects.filter(user_id=user_id)
    serializer = PromptSerializer(promts_for_user, many=True)
    return Response(serializer.data)
