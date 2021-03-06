from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    return render_to_response(
        'startpage/index.html',
        context_instance=RequestContext(request),
    )


def about(request):
    return render_to_response(
        'startpage/about.html',
        context_instance=RequestContext(request),
    )
