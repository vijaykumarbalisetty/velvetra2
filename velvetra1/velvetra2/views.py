import uuid
import os
from django.conf import settings
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from .models import Designer, DesignProject
from .serializers import DesignerSerializer, DesignProjectSerializer

class DesignerViewSet(viewsets.ModelViewSet):
    queryset = Designer.objects.all().order_by('-created_at')
    serializer_class = DesignerSerializer

class DesignProjectViewSet(viewsets.ModelViewSet):
    queryset = DesignProject.objects.all().order_by('-created_at')
    serializer_class = DesignProjectSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        # Allows filtering by id manually to mimic base44.entities.DesignProject.filter({ id: projectId })
        project_id = self.request.query_params.get('id', None)
        if project_id:
            queryset = queryset.filter(id=project_id)
        return queryset

@api_view(['POST'])
def upload_file(request):
    if 'file' not in request.FILES:
        return Response({'error': 'No file uploaded'}, status=status.HTTP_400_BAD_REQUEST)
    
    file = request.FILES['file']
    file_name = f"{uuid.uuid4()}_{file.name}"
    
    # Save file
    path = default_storage.save(file_name, ContentFile(file.read()))
    file_url = request.build_absolute_uri(settings.MEDIA_URL + path)
    
    return Response({'file_url': file_url})

@api_view(['POST'])
def generate_image(request):
    prompt = request.data.get('prompt', '')
    
    replicate_api_token = os.getenv('REPLICATE_API_TOKEN')
    
    if not replicate_api_token:
        # Fallback to placeholder if token is missing
        fake_generated_image_url = f"https://picsum.photos/seed/{hash(prompt) % 10000}/600/600"
        return Response({
            'url': fake_generated_image_url,
            'type': 'ai_generated',
            'status': 'fallback',
            'message': 'REPLICATE_API_TOKEN not set, using placeholder'
        })

    try:
        import replicate
        # Using Stable Diffusion XL (SDXL) for high quality
        output = replicate.run(
            "stability-ai/sdxl:7762fd39731443c6503e2d9ca48207c64636b1d97011a0209e9f3b04a053e14b",
            input={"prompt": prompt}
        )
        # Replicate SDXL output is usually a list of strings (URLs)
        image_url = output[0] if isinstance(output, list) else output
        
        return Response({
            'url': image_url,
            'type': 'ai_generated',
            'prompt': prompt
        })
    except Exception as e:
        return Response({
            'error': str(e),
            'status': 'error',
            'message': 'Failed to generate image via Replicate'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
