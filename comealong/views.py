from project.models import Project
from django.views.generic import TemplateView
from my_user.models import MyUser
from django.contrib.auth import authenticate

class Index(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['new_projects'] = Project.objects.all().order_by("id").reverse()[0:4]
        context['staffpicks_projects'] = [
            Project.objects.get(id=1),
            #Project.objects.get(id=3),
        ]
        return context

def is_username_available(request):
    if MyUser.objects.filter(username=request.username).count() > 0:
        return HttpResponse("False")
    return HttpResponse("True")


def login(request):
    user = authenticate(username=request.username, password=request.password)
    if user is None:
        return HttpResponse("error")
    return HttpResponse("success")

def register(request):
    user = User.objects.create_user(request.username, request.email, request.password, first_name=request.first_name, last_name=request.last_name)
    login(request)
