__title__ = 'debug_toolbar_force.tests.foo.apps'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('Config',)

try:
    from django.apps import AppConfig

    class Config(AppConfig):
        """Config."""

        name = 'debug_toolbar_force.tests.foo'
        label = 'debug_toolbar_force_tests_foo'

except ImportError:
    pass