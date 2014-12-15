from __future__ import print_function, unicode_literals

from os.path import dirname, join as ospj
from tempfile import mkdtemp
import unittest

from DenyHosts.constants import RESTRICTED_USERNAMES
from DenyHosts.prefs import Prefs
from DenyHosts.restricted import Restricted

class EmptyRestrictedTest(unittest.TestCase):
    """
    Tests creating a Restricted object with no data file. This should:
    1) not throw an exception, and
    2) result in an empty set of restricted hosts.

    We ensure that there's no data file by making an empty temporary
    directory for this test, and assinging that path to the appropriate
    Prefs key.
    """
    def setUp(self):
        self.prefs = Prefs()
        self.prefs._Prefs__data['ETC_DIR'] = mkdtemp()

    def test_no_data_file(self):
        restricted = Restricted(self.prefs)
        self.assertFalse(restricted.get_restricted())
