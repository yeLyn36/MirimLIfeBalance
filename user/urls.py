from django.urls import path

from user.views import MilibalLoginView, MilibalAddUserView, MilibalReadUserView, MilibalEditUserView, \
    MilibalDeleteUserView

app_name = 'user'

urlpatterns = [
    path('login/', MilibalLoginView.as_view(), name='login'),  # {% url 'bookmark:list' %}
    path('join/', MilibalAddUserView.as_view(), name='join'),
    path('<pk>', MilibalReadUserView.as_view(), name='detail'),
    path('<pk>/edit', MilibalEditUserView.as_view(), name='update'),
    path('<pk>/delete', MilibalDeleteUserView.as_view(), name="delete"),
]