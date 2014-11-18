from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import  HttpResponseRedirect, HttpResponseForbidden
from django.core.context_processors import csrf

from models import *
from forms import  *

def index(request):
    projects = Project.objects.all().order_by("id").reverse()
    return render_to_response("projects/index.html", RequestContext(request, {"projects" : projects}))

def page(request, id):
    project = Project.objects.get(id=id)

    if(request.POST):
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/projects/" + str(project.id))
    else:
        applications = Application.objects.filter(project_id=id, result='W')
        form = ProjectForm(instance=project)
        return render_to_response("projects/page.html", RequestContext(request, {"project" : project, "applications": applications, "form": form}))

def new(request):
    if(request.POST):
        form = ProjectForm(request.POST, request.FILES)
        if(form.is_valid()):

            obj = form.save(commit=False)
            obj.founder = request.user
            obj.save()

            participation = Participation(project=obj, user=request.user)
            participation.save()

            title = Title(participation=participation, title="Founder")
            title.save()

            return HttpResponseRedirect('/projects/')
    else:
        form = ProjectForm();

    args = {}
    args.update(csrf(request))
    args['form'] = form

    return render_to_response('projects/new.html', RequestContext(request, args))


def application(request, id, app_id):
    project = Project.objects.get(id=id)
    application = Application.objects.filter(id = app_id).first()

    if (not application) or (project.founder != request.user):
        return HttpResponseRedirect('/projects/' + str(project.id))

    if(request.POST):
        form = AcceptApplicationForm(application, request.POST);
        if(form.is_valid()):

            participation = Participation.objects.filter(project=project, user=application.user).first()
            if( not participation):
                participation = Participation(project=application.project, user=application.user)
                participation.save()


            for r in form.cleaned_data["roles"]:
                application.roles.filter(title = r).first().delete()
                title = Title(participation=participation, title=r)
                title.save()

            return HttpResponseRedirect('/projects/' + str(project.id))

    else:
        form = AcceptApplicationForm(application);

    args = {"application": application, "project": project}
    args.update(csrf(request))
    args['form'] = form

    return render_to_response("applications/page.html", RequestContext(request, args))

def apply(request, id):
    project = Project.objects.get(id=id)
    application = Application.objects.filter(project=project, user=request.user).first()

    if(request.POST):
        if(application):
            form = ApplicationForm(project, request.POST, instance=application)
        else:
            form = ApplicationForm(project, request.POST)
        if(form.is_valid()):

            app = form.save(commit=False)
            app.user = request.user
            app.project = project
            app.save()

            for r in app.roles.all():
                r.delete();
            for r in form.cleaned_data["roles"]:
                t = Title(title = r, application = app)
                t.save()

            return HttpResponseRedirect('/projects/')
    else:
        if(application):
            form = ApplicationForm(project, instance = application);
        else:
            form = ApplicationForm(project);

    args = {"project": project,}
    args.update(csrf(request))
    args['form'] = form

    return render_to_response('applications/new.html', RequestContext(request, args))

def recruit(request, id):
    if(request.POST):
        user = request.user
        project = Project.objects.get(id=id)

        if(project.founder == user):
            vacancy = Vacancy(project=project, title=request.POST['title'], total = request.POST['quantity'])
            if(vacancy.isValid()):
                vacancy.save();

    return HttpResponseRedirect('/projects/' + str(project.id))
