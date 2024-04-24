from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ImageSerializer
from .utils import perform_analysis
from django.shortcuts import render
from django.views import View

class CustomImageView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            custom_image_serializer = ImageSerializer(data=request.data)

            if custom_image_serializer.is_valid():
                custom_image_serializer.save()

                # Perform analysis on the uploaded image using a custom analysis utility
                image_path = custom_image_serializer.data['image']
                analysis_result = perform_analysis(image_path)

                return Response({'result': analysis_result['description']}, status=status.HTTP_200_OK)

        except Exception as exception:
            return Response({'message': f'Server Error: {str(exception)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(custom_image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PictureUploadView(View):
    def get(self, request, *args, **kwargs):
        # Render a simple HTML form for image upload to test the functionality of the API endpoint
        return render(request, 'upload_form.html')
