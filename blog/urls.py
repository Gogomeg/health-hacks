from django.urls import path
from .views import Index, PostList, post_detail


urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('<slug:slug>/', PostList.as_view(), name='home'),
]
