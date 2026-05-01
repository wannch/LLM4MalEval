from sample.simple import add_one
if False:
    _var_179_0 = (551, 989, 686)
    _var_179_1 = (484, 820, 690)
    _var_179_2 = (340, 376, 59)

    def _var_179_fn():
        pass
import unittest

class TestSimple(unittest.TestCase):

    def test_add_one(self):
        self.assertEqual(add_one(5), 6)
if __name__ == '__main__':
    unittest.main()