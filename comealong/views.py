#from django.http import HttpResponse
#from django.template.loader import get_template
from django.template import RequestContext
from django.shortcuts import render_to_response
from project.models import Project

#def index(request):
#    context = RequestContext(request, {})
#    template = get_template("index.html")
#    html = template.render(context)
#    return HttpResponse(html)

def index(request):
    staffpicks_projects = [
        Project.objects.get(id=4),
    ]
    new_projects = Project.objects.all().order_by("id").reverse()[0:4]
    return render_to_response("index.html", RequestContext(request, {"new_projects" : new_projects, "staffpicks_projects": staffpicks_projects}))
