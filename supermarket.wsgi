#!/home/users/ogolnopolskie/serwisy/supermarket/.local/bin/python
import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/home/users/ogolnopolskie/serwisy/supermarket/.virtualenvs/supermarket/local/lib/python2.7/site-packages')

# Add the app's directory to the PYTHONPATH
#sys.path.append('/home/users/ogolnopolskie/serwisy/supermarket/supermarket_metodyczny/')
#sys.path.append('/home/users/ogolnopolskie/serwisy/supermarket/supermarket_metodyczny/base/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'supermarketmetodyczny.prod_settings'

# Activate your virtual env
activate_env=os.path.expanduser("/home/users/ogolnopolskie/serwisy/supermarket/.virtualenvs/supermarket/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

from supermarketmetodyczny.wsgi import application

#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()
