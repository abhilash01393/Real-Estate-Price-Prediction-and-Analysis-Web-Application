"""applied_real_estate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url,include
from pricing import views
from pricing.views import index
from pricing.views import about
from pricing.views import login
from pricing.views import blog
from pricing.views import categories
from pricing.views import contact
from pricing.views import forgot
from pricing.views import registration
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
	path('index.html', index),
	path('', index),
	path('accounts/', include('django.contrib.auth.urls')),
	path('about.html', about),
	path('blog.html', blog),
	path('login.html', login),
	path('categories.html', categories),
	path('contact.html', contact),
	path('forgot.html', forgot),
	path('registration.html', registration),
#    url(r'^special/',views.special,name='special'),
    url(r'',include('pricing.urls')),
    url(r'^logout/$', views.logout, name='logout'),
	url(r'^login/$',views.login,name='login'),
	path('', TemplateView.as_view(template_name='index.html'), name='index'), # new
]
