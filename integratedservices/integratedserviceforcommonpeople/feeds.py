from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Service

class LatestServicesFeed(Feed):
    title = "Latest Services"
    link = "/services/feed/"
    description = "Updates on the latest services registered."

    def items(self):
        return Service.objects.order_by('-id')[:10]

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return f"Service Type: {item.service_type}, Location: {item.location}"

    def item_link(self, item):
        return reverse('service_detail', args=[item.pk])
