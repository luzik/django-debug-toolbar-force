__title__ = 'debug_toolbar_force.tests.foo.apps'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'

try:
    from django.apps import AppConfig

    __all__ = ('Config',)

    class Config(AppConfig):
        """Config."""

        name = 'debug_toolbar_force.tests.foo'
        label = 'debug_toolbar_force_tests_foo'

except ImportError:
    pass
