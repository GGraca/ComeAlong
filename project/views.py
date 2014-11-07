from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import  HttpResponseRedirect
from django.core.context_processors import csrf

from models import Project
from forms import  ProjectForm


def page(request, id):
    project = Project.objects.get(id=id)
    return render_to_response("projects/page.html", RequestContext(request, {"project" : project}))

def index(request):
    projects = Project.objects.all()
    return render_to_response("projects/index.html", RequestContext(request, {"projects" : projects}))

def new(request):
    if(request.POST):
        form = ProjectForm(request.POST)
        if(form.is_valid()):
            #form.cleaned_data['founder_id'] = '1';
            form.save()
            return HttpResponseRedirect('/projects/')
    else:
        form = ProjectForm();

    args = {}
    args.update(csrf(request))
    args['form'] = form

    return render_to_response('projects/new.html', args)
