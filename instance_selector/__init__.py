import django


__version__ = "3.0.0"

if django.VERSION < (3, 2):
    default_app_config = "%s.apps.AppConfig" % __name__
