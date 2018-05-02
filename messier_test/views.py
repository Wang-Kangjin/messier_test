from django.http import Http404, HttpResponse
import datetime
from django.template import loader, Context

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def index(request):
    t = loader.get_template('index.html')
    c = {}
    html = t.render(c)
    return HttpResponse(html)