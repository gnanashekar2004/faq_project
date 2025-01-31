from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import FAQ
from .serializers import FAQSerializer

class FAQListView(APIView):
    """
    API endpoint to fetch FAQs
    Supports language selection via ?lang= query parameter
    """

    def get(self, request):
        lang = request.GET.get('lang', 'en')
        cache_key = f'faqs_{lang}'  # Unique cache key for each language
        data = cache.get(cache_key)  # Try retrieving from cache

        if not data:  # If cache is empty, fetch from DB
            faqs = FAQ.objects.all()
            data = [faq.get_translation(lang) for faq in faqs]
            cache.set(cache_key, data, timeout=3600)  # Cache for 1 hour (3600 sec)

        return Response(data)