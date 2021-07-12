from django.shortcuts import render
from django.http import HttpResponse



from django.template import context, loader

#translation
from django.utils.translation import gettext as _

# Create your views here.


def ejemplo(request):
    """Vista ejemplo translate"""
    context={'hello':_('Hello')
    }
    template= loader.get_template("ejemplo.html")
    return HttpResponse(template.render(context,request))
