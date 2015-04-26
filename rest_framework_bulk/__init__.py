__version__ = '0.2.1'
__author__ = 'Miroslav Shubernetskiy'

try:
    from .generics import *  # noqa
    from .mixins import *  # noqa
    from .serializers import *  # noqa
except Exception:
    pass
