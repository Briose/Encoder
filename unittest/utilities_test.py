import unittest
import utilities


class Test(unittest.TestCase):

    def test_assert_valid_key_ok(self):
        utilities.assert_valid_key('fd8484c6-e826-418f-b1ef-2d120a77bb88')
        utilities.assert_valid_key('25685451-0602-418e-8cee-14f4f01647ed')

    def test_assert_valid_key_empty(self):
        self.assertRaises(Exception,
                          utilities.assert_valid_key,
                          '')

    def test_assert_valid_key_short(