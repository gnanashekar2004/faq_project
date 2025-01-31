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
        lang = request.GET.get('lang', 'en') # Get requested language
        faqs = FAQ.objects.all() # Fetch all FAQs
        data = [faq.get_translation(lang) for faq in faqs] # Get translations for each FAQ
        return Response(data) # Return JSON response