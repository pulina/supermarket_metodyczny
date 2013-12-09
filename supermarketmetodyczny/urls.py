from django.conf.urls import patterns, include, url
from django.contrib import admin
import autoload


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^jsreverse/$', 'django_js_reverse.views.urls_js', name='js_reverse'),
    url(r'', include('base.urls')),
)
