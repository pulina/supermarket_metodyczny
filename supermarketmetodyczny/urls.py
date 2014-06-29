from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.decorators.cache import cache_page

from django_js_reverse.views import urls_js

import autoload


admin.autodiscover()

urlpatterns = patterns('',
#    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^jsreverse/$', cache_page(3600)(urls_js), name='js_reverse'),
    url(r'', include('base.urls')),
)
