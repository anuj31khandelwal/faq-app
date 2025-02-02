from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.cache import cache
from .models import FAQ
from .serializers import FAQSerializer

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get_queryset(self):
        """
        Optionally restricting the returned FAQs by filtering against
        query parameters in the URL.
        """
        queryset = FAQ.objects.all()
        search_query = self.request.query_params.get('search', None)
        
        if search_query:
            queryset = queryset.filter(question__icontains=search_query)
        
        return queryset.order_by('-created_at')

    @action(detail=False, methods=['post'])
    def clear_cache(self):
        """
        Clearing the FAQ cache
        """
        cache.clear()
        return Response({'status': 'cache cleared'})
