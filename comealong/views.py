#from django.http import HttpResponse
#from django.template.loader import get_template
from django.template import RequestContext
from django.shortcuts import render_to_response

#def index(request):
#    context = RequestContext(request, {})
#    template = get_template("index.html")
#    html = template.render(context)
#    return HttpResponse(html)

def index(request):
    return render_to_response("index.html", RequestContext(request, {}))
