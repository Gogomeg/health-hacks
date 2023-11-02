from django.urls import path
from .views import Index, PostList


urlpatterns = [
    path('', Index.as_view(), name='blog'),
    path('', PostList.as_view(), name='home'),
]
