from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import  HttpResponseRedirect
from django.core.context_processors import csrf

from models import Project, Application
from forms import  ProjectForm, ApplicationForm


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

def application(request, id, app_id):
    application = Application.objects.get(id=app_id)
    return render_to_response("applications/page.html", RequestContext(request, {"application" : application}))

def new_application(request, id):
    if(request.POST):
        form = ApplicationForm(request.POST)
        if(form.is_valid()):
            #form.cleaned_data['founder_id'] = '1';
            form.save()
            return HttpResponseRedirect('/projects/')
    else:
        form = ApplicationForm();

    args = {}
    args.update(csrf(request))
    args['form'] = form

    return render_to_response('projects/id/new.html', args)
