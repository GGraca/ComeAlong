from django.template import RequestContext
from django.shortcuts import render_to_response

from models import Project


def page(request, id):
    project = Project.objects.get(id=id)
    return render_to_response("projects/page.html", RequestContext(request, {"project" : project}))

def index(request):
    projects = Project.objects.all()
    return render_to_response("projects/index.html", RequestContext(request, {"projects" : projects}))
