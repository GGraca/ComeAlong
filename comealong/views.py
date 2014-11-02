# Create your views here.
from django.template import RequestContext
from django.shortcuts import render, render_to_response

def index(request):
    # Obtain the context from the HTTP request.
    context = RequestContext(request)

    # Render the response and send it back!
    return render_to_response('index.html', context)
