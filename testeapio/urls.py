
from django.urls import path,include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from .views import  test_view


urlpatterns = [
    #path('compress/', compress_view, name='compress-view'),
    path('', test_view, name='test-view')
]