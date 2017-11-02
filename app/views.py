from django.http import StreamingHttpResponse, HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render
import mimetypes

from app import settings
import os

from django.views.decorators.cache import cache_page, cache_control

@cache_page(60 * 15)    # cache this page for 10 minutes
def index(request:HttpRequest):
    context = {
        'title':'Hello',
    }
    return render(request, 'app/subpage.html', context)

@cache_page(60 * 20)
@cache_control(public=True)
def static(request, path):
    filename = settings.STATIC_ROOT + path
    if os.path.isfile(filename):
        with open(filename, 'rb') as fp:
            data = fp.read()
    else:
        return HttpResponse(status=404)
    return HttpResponse(data, content_type=mimetypes.guess_type(filename)[0])