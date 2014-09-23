from django.core.urlresolvers import reverse
from django.contrib.sitemaps import Sitemap
from django.contrib.auth.models import User
from judge.models import Problem


class ProblemSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.8

    def items(self):
        return Problem.objects.all()

    def location(self, obj):
        return reverse('judge.views.problem', args=(obj.code,))


class UserSitemap(Sitemap):
    changefreq = 'hourly'
    priority = 0.5

    def items(self):
        return User.objects.all()

    def location(self, obj):
        return reverse('judge.views.user', args=(obj.username,))


class HomePageSitemap(Sitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return ['judge.views.home']

    def location(self, obj):
        return reverse(obj)


class UrlSitemap(Sitemap):
    def __init__(self, pages):
        self.pages = pages

    def items(self):
        return self.pages

    def location(self, obj):
        return obj['location'] if isinstance(obj, dict) else obj

    def priority(self, obj):
        return obj.get('priority', 0.5) if isinstance(obj, dict) else 0.5

    def changefreq(self, obj):
        return obj.get('changefreq', 'daily') if isinstance(obj, dict) else 'daily'
