import unittest

import led_matrix


class MyTestCase(unittest.TestCase):

    def test_nothing(self):
        self.assertTrue(True)

    def test_properties(self):
        ndl = led_matrix.NDList(shape=(15, 24, 2))
        self.assertEqual(ndl.shape, (15, 24, 2))
        self.assertEqual(ndl.size, 720)

    def test_getitem(self):
        ndl = led_matrix.NDList(shape=(7, 42, 15))
        out = ndl[0, 0]
        self.assertEqual(len(out), 15)
