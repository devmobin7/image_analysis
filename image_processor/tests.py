import io
import pytest
from rest_framework import status
from rest_framework.test import APIRequestFactory
from unittest.mock import patch
from .views import PictureUploadView
from .serializers import ImageSerializer

@pytest.fixture
def test_client():
    return APIRequestFactory()

@patch('image_processor.utils.analyze_image')
@patch('image_processor.utils.encode_image')
@pytest.mark.django_db
def test_successful_image_upload_and_analysis(mock_encode, mock_analyze, test_client):
    # Arrange
    mock_encode.return_value = 'encoded_mock'
    mock_analyze.return_value = {'description': 'Mocked description'}
    image_content = b'mock_image_content'
    image = io.BytesIO(image_content)
    image.name = 'test_image.jpg'
    request = test_client.post('/perform-analysis/', {'image': image}, format='multipart')

    # Act
    response = PictureUploadView.as_view()(request)

    # Assert
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {'description': 'Mocked description'}
    image_serializer = ImageSerializer(data={'image': 'encoded_mock'})
    assert image_serializer.is_valid()

@patch('image_processor.utils.analyze_image')
@patch('image_processor.utils.encode_image')
@pytest.mark.django_db
def test_failed_image_upload(mock_encode, mock_analyze, test_client):
    # Arrange
    mock_encode.return_value = 'encoded_mock'
    mock_analyze.return_value = {'description': 'Mocked description'}
    request = test_client.post('/perform-analysis/', {}, format='multipart')

    # Act
    response = PictureUploadView.as_view()(request)

    # Assert
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'image' in response.data

@patch('image_processor.utils.analyze_image')
@patch('image_processor.utils.encode_image')
@pytest.mark.django_db
def test_failed_image_analysis(mock_encode, mock_analyze, test_client):
    # Arrange
    mock_encode.return_value = 'encoded_mock'
    mock_analyze.side_effect = Exception("Analysis failed")
    image_content = b'mock_image_content'
    image = io.BytesIO(image_content)
    image.name = 'test_image.jpg'
    request = test_client.post('/perform-analysis/', {'image': image}, format='multipart')

    # Act
    response = PictureUploadView.as_view()(request)

    # Assert
    assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
    assert 'Error' in response.data['message']
