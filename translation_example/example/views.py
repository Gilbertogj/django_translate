from django.shortcuts import render
from django.http import HttpResponse



from django.template import context, loader

#translation
from django.utils.translation import gettext as _
from django.utils.translation import LANGUAGE_SESSION_KEY

# Create your views here.


def ejemplo(request):
    """Vista ejemplo translate"""
    # from django.utils import translation
    # user_language = 'es'
    # translation.activate(user_language)
    # request.session[translation.LANGUAGE_SESSION_KEY] = user_language

    # if translation.LANGUAGE_SESSION_KEY in request.session:
    #     del request.session[translation.LANGUAGE_SESSION_KEY]


    context={'hello':_('Hello')
    }
    template= loader.get_template("ejemplo.html")
    return HttpResponse(template.render(context,request))
