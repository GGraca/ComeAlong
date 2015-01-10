from django.shortcuts import render
from django.http import  HttpResponse

def teste(request, project_id):
    return HttpResponse("success!")
