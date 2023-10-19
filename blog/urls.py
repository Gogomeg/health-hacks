from . import views
from django.urls import path, include


# Map URL for the views
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('upload/', views.image_upload_view)
]
