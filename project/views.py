from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.core.context_processors import csrf
from django.views.generic import TemplateView, DetailView, UpdateView, CreateView
from notifications import *

from models import *
from forms import  *

class CreateProjectView(CreateView):
    form_class = ProjectForm
    template_name = "projects/new.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)

        self.object.founder = self.request.user
        self.object.save()

        participation = Participation(project=self.object, user=self.request.user)
        participation.save()

        title = Title(participation=participation, title="Founder")
        title.save()

        return super(CreateView, self).form_valid(form)


class UpdateProjectView(UpdateView):
    template_name = "projects/edit.html"
    form_class = ProjectForm

    def get_object(self):
        return Project.objects.get(id=self.kwargs['id'])

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['participations'] = self.object.positions.all()
        context['followers'] = self.object.followers.all()
        return context


class ProjectPageView(DetailView):
    template_name = "projects/page.html"

    def get_object(self):
        return Project.objects.get(id=self.kwargs['id'])


class ProjectsIndex(TemplateView):
    template_name = "projects/index.html"

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.all().order_by("id").reverse()
        return context


def delete_project(request, id):
    project = Project.objects.get(id=id)
    if(request.user != project.founder):
        return HttpResponseRedirect('/projects/' + str(project.id))

    if(request.POST):
        project.delete()

        return HttpResponseRedirect('/projects')

    return render_to_response("projects/delete.html", RequestContext(request, {"project": project}))


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
                v = project.vacancies.filter(title = r).first()
                v.available -= 1
                v.save()

                title = Title(participation=participation, title=r)
                title.save()

            notify.send(project.founder, recipient=participation.user, verb="accepted your application for", action_object=project)

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

    if(not project.has_vacancies()):
        return HttpResponseRedirect('/projects/' + str(project.id))

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

            notify.send(request.user, recipient=project.founder, verb="applied for", action_object=project)
            if(request.user.projects_following.filter(id=project.id).count() == 0):
                request.user.projects_following.add(project)

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
    user = request.user
    project = Project.objects.get(id=id)

    if(request.POST):
        if(project.founder == user):
            vacancy = Vacancy(project=project, title=request.POST['title'], total = request.POST['quantity'])
            if(vacancy.isValid()):
                vacancy.save();

                for u in project.followers.all():
                    notify.send(project, recipient=u, verb="is recruiting", action_object=vacancy)



    return HttpResponseRedirect('/projects/' + str(project.id))

def follow(request, id):
    project = Project.objects.get(id=id)
    user = request.user

    if(request.POST):
        if(project.founder != user):
            user.projects_following.add(project)

    return HttpResponseRedirect('/projects/' + str(project.id))

def unfollow(request, id):
    project = Project.objects.get(id=id)
    user = request.user

    if(request.POST):
        if(request.user.projects_following.filter(id=project.id).count()):
            request.user.projects_following.remove(project)

    return HttpResponseRedirect('/projects/' + str(project.id))

def applications(request, id):
    project = Project.objects.get(id=id)
    user = request.user

    if(project.founder == user):
        return render_to_response('applications/new.html', RequestContext(request, {"applications": project.applications.filter(result='W')}))
    return HttpResponseRedirect('/projects/' + str(project.id))


#Vacancies
class CreateVacancyView(CreateView):
    form_class = VacancyForm

    def form_valid(self, form):
        project = Project.objects.get(id=self.kwargs['id'])
        user = self.request.user

        if(self.request.user == project.founder):
            self.object = form.save(commit=False)
            self.object.project = project
            self.object.save()

            return super(CreateView, self).form_valid(form)
        else:
            return HttpResponseForbidden()
