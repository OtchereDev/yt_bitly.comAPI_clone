from api.views import ShortenerCreateApiView, ShortenerListAPIView
from django.urls import path

app_name='api'

urlpatterns = [
    path('',ShortenerListAPIView.as_view(),name='all_links'),
    path('create/',ShortenerCreateApiView.as_view(),name='create_api'),
]
