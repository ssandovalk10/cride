from rest_framework.decorators import api_view
from rest_framework.response import Response

from cride.circles.models import Circle

#Serializer
from cride.circle.serializer import (
    CircleSerializer,
    CreateCircleSerializer)

@api_view(['GET'])
def list_circles(request):
    circles = Circle.objects.filters(is_public=True)
    serializer = CircleSerializer(circles, many=True )    
    return Response(serializer.data)

@api_view(['POST'])
def create_circle(request):
    serializer=CreateCircleSerializer(data=request.data)
    serializer.is_valid(raiseeExeption=True)
    data = serializer.data
    return Response(data)
    