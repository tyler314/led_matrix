import unittest
from random import random
import led_matrix


class test_NDList(unittest.TestCase):

    def test_init(self):
        ndl = led_matrix.NDList(shape=(0,))
        self.assertEqual(ndl, [])

        ndl = led_matrix.NDList(shape=(1,))
        self.assertEqual(ndl, [0.0])

        ndl = led_matrix.NDList(shape=(17, 7, 41, 90, 1))
        ndl_list = [[[[[0.0 for _ in range(1)] for _ in range(90)] for _ in range(41)] for _ in range(7)] for _ in range(17)]
        self.assertEqual(ndl, ndl_list)

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
        # Test a single embedded list
        num = random() * 10
        ndl = led_matrix.NDList(shape=(1,), fill=num)
        self.assertEqual(ndl[0], num)

        # Test a 10x10 array
        num = random() * 10
        ndl = led_matrix.NDList(shape=(10,10), fill=num)      
        for i in range(10):
            for j in range(10):
                self.assertEqual(ndl[i,j], num)

        # Test a 4x4x4 array
        num = random() * 10
        ndl = led_matrix.NDList(shape=(5,5,5), fill=num)
        for i in range(5):
            for j in range(5):
                for k in range(5):
                    self.assertEqual(ndl[i,j,k], num)
        
        # Advanced Test
        num = random() * 10
        ndl = led_matrix.NDList(shape=(17, 7, 41, 90, 1), fill=num)
        for i in range(17):
            for j in range(7):
                for k in range(41):
                    for l in range(90):
                        for m in range(1):
                            self.assertEqual(ndl[i, j, k, l, m], num)

    @unittest.expectedFailure
    def test_setitem(self):
        # Test an array with a single element
        ndl = led_matrix.NDList(shape=(1,))
        ndl[0] = 7
        self.assertEqual(ndl[0], 7)
        
        # Test a single embedded list
        ndl = led_matrix.NDList(shape=(1,1))
        ndl[0,0] = 7
        self.assertEqual(ndl[0,0], 7)

        # Test a 5x5 array
        ndl = led_matrix.NDList(shape=(5,5))      
        for i in range(5):
            for j in range(5):
                num = random() * 10
                ndl[i,j] = num
                self.assertEqual(ndl[i,j], num)

        # Test a 4x4x4 array
        ndl = led_matrix.NDList(shape=(4,4,4))
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    num = random() * 10
                    ndl[i,j,k] = num
                    self.assertEqual(ndl[i,j,k], num)
                    
        # Test array with varrying dimensions
        ndl = led_matrix.NDList(shape=(2, 4))
        for i in range(2):
            for j in range(4):
                num = random() * 10
                ndl[i, j] = num
                self.assertEquals(ndl[i,j], num)
        
        # Advanced Test
        ndl = led_matrix.NDList(shape=(17, 7, 41, 90, 1, 23, 2))
        for i in range(17):
            for j in range(7):
                for k in range(41):
                    for l in range(90):
                        for m in range(1):
                            for n in range(23):
                                for o in range(2):
                                    num = random() * 10
                                    ndl[i, j, k, l, m, n, o] = num
                                    self.assertEqual(ndl[i, j, k, l, m, n, o], num)
            
            
            
            
            
            
            
            
            
            
            
            
            
