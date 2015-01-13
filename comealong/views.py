from project.models import Project
from django.views.generic import TemplateView
from my_user.models import MyUser
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect

class Index(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['new_projects'] = Project.objects.all().order_by("id").reverse()[0:4]
        context['staffpicks_projects'] = [
            #Project.objects.get(id=1),
            #Project.objects.get(id=3),
        ]
        return context

class About(TemplateView):
    template_name = "about.html"

class Features(TemplateView):
    template_name = "features.html"

def is_username_available(request):
    if(request.POST):
        if MyUser.objects.filter(username=request.POST["username"]).count() > 0:
            return HttpResponse("False")
        return HttpResponse("True")
    return HttpResponse("error")

def login_view(request):
    if(request.POST):
        f = request.POST
        user = authenticate(username=f['username'], password=f['password'])
        if user is not None:
            login(request, user)
            #return HttpResponse("success", status=200)
            return HttpResponseRedirect('/')
    return HttpResponse("error")

def register_view(request):
    if(request.POST):
        f = request.POST
        if not (MyUser.objects.get(username=f['username']) or MyUser.objects.get(email=f['email'])):
            user = MyUser(f['username'], f['email'], f['password'], first_name=f['firstname'], last_name=f['lastname'])
            user.save()
            return HttpResponse("success", status=200)
    return HttpResponse("error")
