from . import views
from django.urls import path, include
from .views import AddHack, HealthHack, HackDetail, DeleteHack, EditHack


# Map URL for the views
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('upload/', views.image_upload_view),
    path('add/', AddHack.as_view(), name='add_health_hack'),
    path('', HealthHack.as_view(), name='health_hacks'),
    path('<slug:pk>/', HackDetail.as_view(), name='post_detail'),
    path('delete/<slug:pk>/', DeleteHack.as_view(), name='delete_health_hack'),
    path('edit/<slug:pk>/', EditHack.as_view(), name='edit_health_hack'),
]
