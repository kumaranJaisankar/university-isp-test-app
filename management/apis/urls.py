


from django.contrib import admin
from django.urls import path,include

from openwisp_radius.urls import get_urls
from management.apis.views import GetRadLogAuth

urlpatterns = [
    # ... other urls in your project ...

    # django admin interface urls
    path('check/<str:username>', GetRadLogAuth.as_view(),name="log authe"),
    # openwisp-radius urls
 
]