# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest
nm=unittest.main
np=unittest.TestCase

from sample.simple import add_one


class nG(np):

    def nu(nV):
        nV.assertEqual(add_one(int("".join([chr(53)]))                                ),int("".join([chr(54)]))                                    )


if __name__ ==("".join([chr(95),chr(95),chr(109),chr(97),chr(105),chr(110),chr(95),chr(95)]))                         :
    nm()
