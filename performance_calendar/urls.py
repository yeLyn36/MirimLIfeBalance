from django.urls import path

from performance_calendar import views
from performance_calendar.views import Milibal, MilibalCalenderView

app_name = 'performance_calender'

urlpatterns = [
    path('', views.Milibal, name='index'),  # {% url 'bookmark:list' %},
    path('calendar', MilibalCalenderView.as_view(), name='calendar'),
]