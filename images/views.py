
import random

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Image
from .serializers import ImageSerializer
from rest_framework import viewsets


@api_view(['POST'])
def upload_image(request):
    serializer = ImageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Image uploaded successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_random_image(request):
    images = Image.objects.all()
    if images:
        random_image = random.choice(images)
        serializer = ImageSerializer(random_image)
        print(serializer.data)
        return Response(serializer.data)
    return Response({'message': 'No images available'}, status=status.HTTP_404_NOT_FOUND)
