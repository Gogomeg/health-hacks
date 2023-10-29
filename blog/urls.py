from . import views
from django.urls import path, include
from .views import AddHack, HealthHack


# Map URL for the views
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('upload/', views.image_upload_view),
    path('', AddHack.as_view(), name='add_health_hack'),
    path('health_hacks/', HealthHack.as_view(), name='health_hacks'),
]
