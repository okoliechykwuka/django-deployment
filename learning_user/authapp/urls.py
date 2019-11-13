from django.conf.urls import url
from authapp import views

# TEMPLATE URLS!

app_name = 'authapp'

urlpatterns = [
    url(r'^register/$', views.register, name = 'register'),
    url(r'^user_login/$',views.user_login, name = 'user_login'),
]
