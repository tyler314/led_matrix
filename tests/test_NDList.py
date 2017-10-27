import unittest

import led_matrix


class test_NDList(unittest.TestCase):

    def test_shape(self):
        ndl = led_matrix.NDList(shape=(0,))
        self.assertEqual(ndl, [])
        ndl = led_matrix.NDList(shape=(17,))
        self.assertEqual(ndl.shape, (17,))
        ndl = led_matrix.NDList(shape=(71, 17, 303))
        self.assertEqual(ndl.shape, (71, 17, 303))

    def test_size(self):
        ndl = led_matrix.NDList(shape=(0,))
        self.assertEqual(ndl.size, 0)
        ndl = led_matrix.NDList(shape=(1,))
        self.assertEqual(ndl.size, 1)
        ndl = led_matrix.NDList(shape=(15, 24, 2))
        self.assertEqual(ndl.size, 720)

    def test_getitem(self):
        ndl = led_matrix.NDList(shape=(10, 10, 10), fill=1)
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    self.assertEqual(ndl[i, j, k], 1)

    @unittest.expectedFailure
    def test_setitem(self):
        ndl = led_matrix.NDList(shape=(1,))
        ndl[0] = 7
        self.assertEqual(ndl[1], 7)
