from . import views
from django.urls import path, include
from .views import AddHack, HealthHackView, HackDetail, DeleteHack, EditHack
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static


# Map URL for the views
urlpatterns = [
    path('add/', AddHack.as_view(), name='add_health_hack'),
    path('', HealthHackView.as_view(), name='health_hacks'),
    path('<slug:pk>/', HackDetail.as_view(), name='post_detail'),
    path('delete/<slug:pk>/', DeleteHack.as_view(), name='delete_health_hack'),
    path('edit/<slug:pk>/', EditHack.as_view(), name='edit_health_hack'),
    path("", include("blog.urls")),
    path("admin/", admin.site.urls),
    path("summernote/", include("django_summernote.urls")),
    path("accounts/", include("allauth.urls")),
    path("djrichtextfield/", include("djrichtextfield.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
