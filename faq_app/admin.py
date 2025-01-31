from django.contrib import admin
from .models import FAQ

class FAQAdmin(admin.ModelAdmin):
    list_display = ('question',) # show only questions in the admin panel

admin.site.register(FAQ, FAQAdmin)

