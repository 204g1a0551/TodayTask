from django.shortcuts import render
from django.http import HttpResponse
def fun1(request,name):
    return HttpResponse(f"<h1 align='center'>Dynamic Johnny Rhyme </h1><br><hr><p><strong>Father:</strong> {name}!! {name}!!<br><strong>{name}:</strong> Yes Papa!!<br><strong>Father:</strong> Eating Sugar?<br><strong>{name}:</strong> No Papa!!<br><strong>Father:</strong> Telling lies<br><strong>{name}:</strong> No Papa!<br><strong>Father:</strong> Open your mouth!<br><strong>{name}:</strong> Hahaha!!!!!!!!!!</p>")
