import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import FAQ

@pytest.mark.django_db
class TestFAQAPI:
    @pytest.fixture
    def api_client(self):
        return APIClient()
    
    @pytest.fixture
    def faq_instance(self):
        return FAQ.objects.create(
            question="What is Django?",
            answer="Django is a web framework."
        )
    
    def test_list_faqs(self, api_client, faq_instance):
        url = reverse('faq-list')
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) == 1
    
    def test_create_faq(self, api_client):
        url = reverse('faq-list')
        data = {
            'question': 'Test Question',
            'answer': 'Test Answer'
        }
        response = api_client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert FAQ.objects.count() == 1
    
    def test_get_faq_with_language(self, api_client, faq_instance):
        url = reverse('faq-detail', kwargs={'pk': faq_instance.pk})
        response = api_client.get(f"{url}?lang=hi")
        assert response.status_code == status.HTTP_200_OK
        assert 'question' in response.data
        assert 'answer' in response.data
        assert 'language' in response.data
        assert response.data['language'] == 'hi'