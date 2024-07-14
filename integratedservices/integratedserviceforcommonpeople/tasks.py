# services/tasks.py
from celery import shared_task
import feedparser
from .models import Service

RSS_FEED_URL = 'http://127.0.0.1:8000/services/feed/'

@shared_task
def update_services_from_rss():
    feed = feedparser.parse(RSS_FEED_URL)
    for entry in feed.entries:
        name = entry.get('title', 'Default Name')
        location = entry.get('location', 'Default Location')
        service_type = entry.get('service_type', 'Default Type')
        mobile_number = entry.get('mobile_number', '0000000000')
        email = entry.get('email', 'default@example.com')
        whatsapp_number = entry.get('whatsapp_number', '0000000000')
        website = entry.get('link', '')
        address = entry.get('address', '')

        service, created = Service.objects.update_or_create(
            name=name,
            defaults={
                'location': location,
                'service_type': service_type,
                'mobile_number': mobile_number,
                'email': email,
                'whatsapp_number': whatsapp_number,
                'website': website,
                'address': address,
            }
        )
