from django.contrib import admin
from .models import FAQ

class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')  # Display questions and answers in admin panel
    search_fields = ('question',)  # Enable search by question
    list_filter = ('question',)  # Allow filtering FAQs

admin.site.register(FAQ, FAQAdmin)
