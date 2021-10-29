from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class Static_Sitemap(Sitemap):

    priority = 1.0
    changefreq = 'daily'


    def items(self):
        return ['index']

    def location(self, item):
        return reverse(item)

