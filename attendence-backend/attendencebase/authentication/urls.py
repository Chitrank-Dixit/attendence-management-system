from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'user-login/$', views.LoginView.as_view(), name='user_login'),
    url(r'user-logout/$', views.LogoutView.as_view(), name='user_logout'),

]