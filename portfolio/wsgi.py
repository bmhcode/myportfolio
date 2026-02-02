
# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

# application = get_wsgi_application()




import os
import sys


path2 = '/home/bmhcodes/portfolio/portfolio'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'portfolio.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
