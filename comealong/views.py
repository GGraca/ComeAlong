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
    new_projects = Project.objects.all().order_by("id").reverse()
    return render_to_response("index.html", RequestContext(request, {"new_projects" : new_projects}))
