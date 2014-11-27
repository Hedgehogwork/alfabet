from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponsePermanentRedirect
from django.views.generic.base import View, TemplateView
from django.views.generic import View
from django.views.generic.edit import FormView
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django import forms

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from uploadapp.form import *
# Create your views here.

class UploadAlfabet(View):

    """
    This view handles Personal Area login requests.
    """
    def post(self, request):

        return render(request, 'upload_alfabet.html',
                {})

    def get(self, request):
        gets = 1
        form = UploadFileForm()
        return render(request, 'upload_alfabet.html',
                               {'gets': gets,
                               'form': form,
                                })

