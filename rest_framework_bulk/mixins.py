from __future__ import print_function, unicode_literals
import rest_framework


# import appropriate mixins depending on the DRF version
# this allows to maintain clean code for each DRF version
# without doing any magic
# a little more code but a lit clearer what is going on
if str(rest_framework.__version__).startswith('2'):
    from .drf2.mixins import *  # noqa
else:
    from .drf3.mixins import *  # noqa
