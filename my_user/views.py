from django.shortcuts import render
from django.http import HttpResponse

from django.template import RequestContext
from django.shortcuts import render_to_response

from models import MyUser



# Create your views here.
def user(request, username):
    return HttpResponse(MyUser.objects.get(username=username).get_full_name())

def all(request):
    html = ""
    users = MyUser.objects.all()

    for u in users:
        html += u.username + "<p>";

    return HttpResponse(html)
    #return render_to_response("index.html", RequestContext(request, {"users" : MyUser.objects.all()}))
