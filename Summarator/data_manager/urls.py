from django.conf.urls import url
from . import views

 
urlpatterns = [
    url(r'(?P<scraper>.*)/$', views.Scrape.as_view()),
]