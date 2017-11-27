import unittest
import lab4

class TestFoo(unittest.TestCase):

    def setUp(self):
        self.result1, self.result2    = lab4.foo(2, 3)
        self.result3, self.result4    = lab4.foo(5, 1)

        self.result5, self.result6    = lab4.foo(-1, 6)
        self.result7, self.result8    = lab4.foo(2, -5)

        self.result9, self.result10   = lab4.foo(-2, -5)
        self.result11, self.result12  = lab4.foo(0, -3)

        self.result13, self.result14  = lab4.foo(2.3, 4.7)
        self.result15, self.result16  = lab4.foo(1.85, 8.97)

        self.result17, self.result18  = lab4.foo(-6.34, 3.5)
        self.result19, self.result20  = lab4.foo(-1.85, 8.97)

        self.result21, self.result22  = lab4.foo(-6.34, -3.5)
        self.result23, self.result24  = lab4.foo(-2.44, -4.5)

    def tearDown(self):
        pass

    def test_positive_int(self):
        self.assertEquals(self.result1, 2.5)
        self.assertEquals(self.result2, 2)
        self.assertEquals(self.result3, 3)
        self.assertEquals(self.result4, 3)

    def test_semipos_int(self):
        self.assertEquals(self.result5,2.5)
        self.assertEquals(self.result6, 2)
        self.assertEquals(self.result7,-1.5 )
        self.assertEquals(self.result8,-2 )

    def test_negative_int(self):
        self.assertEquals(self.result9,  -3.5)
        self.assertEquals(self.result10, -4)
        self.assertEquals(self.result11, -1.5)
        self.assertEquals(self.result12, -2)

    def test_positive_float(self):
        self.assertEquals(self.result13, 3.5)
        self.assertEquals(self.result14, 4)
        self.assertEquals(self.result15, 5.41)
        self.assertEquals(self.result16, 5)

    def test_semipos_float(self):
        self.assertEquals(self.result17, -1.42)
        self.assertEquals(self.result18, -1)
        self.assertEquals(self.result19, 3.5600000000000005)
        self.assertEquals(self.result20, 4)

    def test_negative_float(self):
        self.assertEquals(self.result21, -4.92)
        self.assertEquals(self.result22, -5)
        self.assertEquals(self.result23, -3.4699999999999998)
        self.assertEquals(self.result24, -3)

