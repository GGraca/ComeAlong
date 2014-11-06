from django.template import RequestContext
from django.shortcuts import render_to_response

from models import MyUser


def page(request, username):
    this_user = MyUser.objects.get(username=username)
    return render_to_response("users/page.html", RequestContext(request, {"this_user" : this_user}))

def index(request):
    users = MyUser.objects.all()
    return render_to_response("users/index.html", RequestContext(request, {"users" : users}))
