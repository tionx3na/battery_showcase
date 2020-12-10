from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class StaticViewsSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1.0


    def items(self):
        return ['landing', 'main_app', 'showcase', 'contact', 'amaron', 'about']

    def location(self, item):
        return reverse(item)

    