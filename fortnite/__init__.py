# -*- coding: utf-8 -*-

"""
Fortnite-TRN-Wrapper
~~~~~~~~
A hopefully good FortniteTrackerNetwork API Wrapper
"""

import logging
from collections import namedtuple
from .utils.platforms import Platforms
from .client import Client

__title__ = 'Fortnite-TRN-Wrapper'
__author__ = 'Matthias K.'
__version__ = '0.0.1a'
__license__ = 'GNU General Public License v3.0'
__copyright__ = '(c) 2019 Matthias K.'
__url__ = 'https://github.com/byWambo/Fortnite-TRN-Wrapper'

VersionInfo = namedtuple('VersionInfo', 'major minor micro releaselevel serial')
version_info = VersionInfo(major=0, minor=0, micro=1, releaselevel='alpha', serial=0)

fmt = '[%(levelname)s] %(asctime)s - %(name)s:%(lineno)d - %(message)s'
logging.basicConfig(format=fmt, level=logging.INFO)
logging.getLogger(__name__).addHandler(logging.NullHandler())
