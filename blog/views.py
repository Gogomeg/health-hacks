from django.views.generic import ListView
from health_hacks.models import HealthHack

class Index(ListView):
    template_name = 'blog/index.html'
    model = HealthHack
    context_object_name = 'health_hacks'

    def get_queryset(self):
        return self.model.objects.all()[:3]
