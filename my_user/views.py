from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import  HttpResponseRedirect, HttpResponseForbidden
from django.views.generic import View

from models import MyUser
from forms import MyUserForm

class MyUserView(View):
    def get(self, request):
        pass


def page(request, username):
    this_user = MyUser.objects.get(username=username)
    return render_to_response("users/page.html", RequestContext(request, {"this_user" : this_user}))

def edit(request, username):
    this_user = MyUser.objects.get(username=username)
    if(request.user != this_user):
        return HttpResponseRedirect("/users/" + this_user.username)

    if(request.POST):
        form = MyUserForm(request.POST, request.FILES, instance=this_user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/users/" + this_user.username)
    else:
        form = MyUserForm(instance=this_user)
        return render_to_response("users/edit.html", RequestContext(request, {"this_user" : this_user, "form": form}))

def index(request):
    users = MyUser.objects.all()
    return render_to_response("users/index.html", RequestContext(request, {"users" : users}))
