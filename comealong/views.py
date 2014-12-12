from project.models import Project
from django.views.generic import TemplateView

class Index(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['new_projects'] = Project.objects.all().order_by("id").reverse()[0:4]
        context['staffpicks_projects'] = [
            Project.objects.get(id=2),
            Project.objects.get(id=3),
        ]
        return context
