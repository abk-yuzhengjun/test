from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime


# Create your views here.
def index2(request):
    return render(request, 'index.html')

def index(request):
    context = {}
    context['hello'] = 'Hello World!!!'
    return render(request, 'index2.html',context)

def current_datetime(request):
    now = datetime.datetime.now()
    html = '<html>' \
           '<body>' \
           'It is now %s.' \
           '</body>' \
           '</html>' % now
    return HttpResponse(html)


def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()

    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    assert False
    html = '<html>' \
           '<body>' \
           'in %s hour(s) It will be %s.' \
           '</body>' \
           '</html>' % (offset,dt)
    return HttpResponse(html)
