from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import ListView

from performance_calendar.models import Event


def Milibal(request):
    template = loader.get_template('performance_calendar/milibal.html')
    context = {
        'index': ""
    }
    return HttpResponse(template.render(context, request))


class MilibalCalenderView(ListView):
    model = Event
    field = '__all__'
    template_name = 'performance_calendar/milibal_calendar.html'