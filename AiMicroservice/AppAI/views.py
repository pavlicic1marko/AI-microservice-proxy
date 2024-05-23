import django
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from AppAI.models import Prompt
from AppAI.serializer import PromptSerializer
import django.core.exceptions


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
@permission_classes([AllowAny])

def getPrompts(request,pk):
    user_id = 1
    promts_for_user = Prompt.objects.filter(user_id=user_id)
    serializer = PromptSerializer(promts_for_user, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
# @permission_classes([IsAdminUser])
def deletePromptById(request, pk):
    prompt_id = pk
    try:
        prompt = Prompt.objects.filter(_id=prompt_id)
        prompt.delete()
        return Response('prompt is deleted', status=200)

    except django.core.exceptions.ObjectDoesNotExist:
        return Response('prompt does not exist', status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        return Response(e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def createPrompt(request):
    data = request.data
    api_Response = 'test_Response'

    try:
        prompt = Prompt.objects.create(
            user_id = 1,
            question='test',
            answer=api_Response,
        )
        serializer = PromptSerializer(prompt, many=False)
        return Response(serializer.data)


    except:
        message = {'detail': 'SERVER ERROR'}
        return Response(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

