from django.conf.urls import url
from pricing import views
# SET THE NAMESPACE!
app_name = 'pricing'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
#    url(r'^login/$',views.login,name='login'),
]