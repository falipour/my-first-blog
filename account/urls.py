from django.conf.urls import url
from . import views
from django.contrib.auth.views import logout

app_name = 'account'

urlpatterns = [
    # /auth/register/
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # /auth/login
    url(r'^login/$', views.UserLoginView.as_view(), name='login'),

    # /auth/logout
    url(r'^logout/$', logout, {'next_page': 'account:login'}, name='logout')
]
