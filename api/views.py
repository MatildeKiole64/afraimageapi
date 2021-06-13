from rest_framework import status
from django.shortcuts import render
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from PIL import Image, ImageSequence
from .serializers import *
from io import BytesIO
from rest_framework import renderers
import base64


# Create your views here.

class JPEGRenderer(renderers.BaseRenderer):
    media_type = 'image/*'
    format = 'jpg'
    charset = None
    render_style = 'binary'

    def render(self, data, media_type=None, renderer_context=None):
        return data

@api_view(['POST', 'GET'])
@renderer_classes((JPEGRenderer,))
def compress_view(request):
    serializer = ImageSerializer(data=request.data)
    if serializer.is_valid():
        img = request.data.get('img')
        compressImageInBytes = BytesIO()
        image = Image.open(img)
        image.save(compressImageInBytes, format='JPEG',
                   quality=serializer.validated_data['quality'])
        compressed_img = compressImageInBytes.getvalue()
        return Response(compressed_img, content_type = "image/jpeg", status=status.HTTP_200_OK)
    return Response({}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST', 'GET'])
def compress_gif_view(request):
    
    image_in_bytes = BytesIO()
    serializer = ImageSerializer(data=request.data)

    if serializer.is_valid():
            img = Image.open(request.data.get('img'))
            image = Image.open(img)
            frames = ImageSequence.Iterator(image)
            for frame in frames:
                frame.save(image_in_bytes, format='JPEG',
                   quality=serializer.validated_data['quality'])
                
    return Response({}, status=status.HTTP_400_BAD_REQUEST)

def test_view(request):
    return render(request, 'api/test.html', {})
