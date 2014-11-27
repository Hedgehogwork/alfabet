from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponsePermanentRedirect
from django.views.generic.base import View, TemplateView
from django.views.generic import View
from django.views.generic.edit import FormView
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django import forms

# Create your views here.
def home(request):
    gets = 00000
    return render(request, 'upload_alfabet.html',
                               {'gets': gets, })