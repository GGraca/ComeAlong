from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import  HttpResponseRedirect, HttpResponseForbidden
from django.core.context_processors import csrf

from models import Project, Application
from forms import  ProjectForm, ApplicationForm

def index(request):
    projects = Project.objects.all()
    return render_to_response("projects/index.html", RequestContext(request, {"projects" : projects}))

def page(request, id):
    project = Project.objects.get(id=id)

    if(request.POST):
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/projects/" + str(project.id))
    else:
        applications = Application.objects.filter(project_id=id)
        form = ProjectForm(instance=project)
        return render_to_response("projects/page.html", RequestContext(request, {"project" : project, "applications": applications, "form": form}))

def new(request):
    if(request.POST):
        form = ProjectForm(request.POST, request.FILES)
        if(form.is_valid()):

            obj = form.save(commit=False)
            obj.founder = request.user
            obj.save()

            return HttpResponseRedirect('/projects/')
    else:
        form = ProjectForm();

    args = {}
    args.update(csrf(request))
    args['form'] = form

    return render_to_response('projects/new.html', RequestContext(request, args))

def application(request, id, app_id):
    application = Application.objects.get(id=app_id, project_id=id)
    if(application != None):
        return render_to_response("applications/page.html", RequestContext(request, {"application" : application}))

def new_application(request, id):
    if(request.POST):
        form = ApplicationForm(request.POST)
        if(form.is_valid()):

            obj = form.save(commit=False)
            obj.user = request.user
            obj.project = Project.objects.get(id=id)
            obj.save()

            return HttpResponseRedirect('/projects/')
    else:
        form = ApplicationForm();

    args = {"project_id": id}
    args.update(csrf(request))
    args['form'] = form

    return render_to_response('applications/new.html', RequestContext(request, args))
