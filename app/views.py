from django.http import StreamingHttpResponse, HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render
import mimetypes

from app import settings
import os

from django.views.decorators.cache import cache_page


def index(request:HttpRequest):
    context = {
        'title':'Hello',
        'body':'How\'s it going?'
    }
    return render(request, 'index.html', context)


def static(request, path):
    filename = settings.STATIC_ROOT
    if os.path.isfile(filename):
        with open(filename, 'rb') as fp:
            data = fp.read()
    else:
        return HttpResponse(status=404)
    return HttpResponse(data, content_type=mimetypes.guess_type(filename))