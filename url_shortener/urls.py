from django.urls import path
from shortener.views import URLListCreateAPIView, URLRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('url/', URLListCreateAPIView.as_view()),
    path('url/<int:pk>/', URLRetrieveUpdateDestroyAPIView.as_view()),
]
