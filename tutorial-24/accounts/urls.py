from django.conf.urls import url
from . import views
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.contrib.auth.views import password_reset
from django.contrib.auth.views import password_reset_done
from django.contrib.auth.views import password_reset_confirm
from django.contrib.auth.views import password_reset_complete



urlpatterns = [
    url(r'^$', views.home),

    # Allows to render our own login page
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}),
    url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'}),
    url(r'register/$', views.register, name='register'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^change-password/$', views.change_password, name='change_password'),
    url(r'^reset-password/$', password_reset, name='reset_password'),
    url(r'^reset-password-done$', password_reset_done, name='password_reset_done'),
    #url(r'^reset-password/confirm$', password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset-password/complete$', password_reset_complete, name='password_reset_complete'),

]

# url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
#     name='password_reset_confirm')

# python -m smtpd -n -c DebuggingServer localhost:1025
# and adjust your mail settings accordingly:
# EMAIL_HOST = 'localhost'
# EMAIL_PORT = 1025
