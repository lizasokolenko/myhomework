import unittest


from vector import Vector
from math import sqrt


class TestVector(unittest.TestCase):

    @staticmethod
    def _get_vector():
        return Vector([1, 2, 3, 4])

    def test_str(self):

        v = self._get_vector()
        self.assertEqual(str(v), "Vector([1, 2, 3, 4])")

        v = Vector([1, 1, -1])
        self.assertEqual(str(v), "Vector([1, 1, -1])")

        self.assertNotEqual(str(Vector([1, 1, -1])), [1, 1, -1])

    def test_repr(self):
        v = Vector([1, 2, 3])

        self.assertEqual(str(v), "Vector([1, 2, 3])")
        self.assertEqual(repr(v), str(v))

        v = Vector([1.0, 2, 3.0])

        self.assertEqual(str(v), "Vector([1.0, 2, 3.0])")
        self.assertEqual(repr(v), str(v))

    def test_add(self):
        v = Vector([2, 2, 0])
        p = Vector([1, 2, 3])
        r = Vector([0, 1, 0])

        self.assertEqual(v + r + p, Vector([3, 5, 3]))

        self.assertEqual(v + v + p, Vector([5, 6, 3]))

        c = Vector([2, 8])
        with self.assertRaises(IndexError):
            (v + c)

    def test_sub(self):
        v = Vector([2, 2, 0])
        p = Vector([1, 2, 3])
        r = Vector([0, 1, 0])

        self.assertEqual(v - r + p, Vector([3, 3, 3]))

        self.assertNotEqual(v - r, 'Vector([2, 1, 0])')

        c = Vector([2, 8])
        with self.assertRaises(IndexError):
            (v - c)

    def test_mul(self):
        v = Vector([2, 2, 0])
        p = Vector([1, 2, 3])

        self.assertEqual(v * p, 'Vector([2, 4, 0])')

        self.assertNotEqual(v * p, Vector([2, 4, 0]))

        with self.assertRaises(TypeError):
            (2 * p * p)

    def test_truediv(self):
        v = Vector([2, 2, 0])
        r = Vector([0, 1, 0])

        self.assertEqual(v / r, 'Vector([0.0, 2.0, 0.0])')

        self.assertNotEqual(r / v, Vector([0.0, 0.5, 0.0]))

        c = Vector([2, 8])
        with self.assertRaises(IndexError):
            (v / c)

    def test_len(self):
        v = self._get_vector()
        self.assertEqual(len(v), 4)

        v = Vector([1, 1, -1])
        self.assertNotEqual(len(v), 3.4)

        c = Vector([2, 8])
        self.assertNotEqual(len(v), len(c))

    def test_append(self):
        v = self._get_vector()

        v.append(5)
        self.assertEqual('Vector([1, 2, 3, 4, 5])', str(v))

        v.append(6)
        self.assertEqual(v.ndim(), 6)

        for n in range(0, 10):
            v.append(n)

        self.assertEqual(v.ndim(), 16)

    def test_abs(self):
        v = self._get_vector()
        c = Vector([4, 3, 2, 1])

        self.assertEqual(abs(v) == sqrt(1 + 4 + 9 + 16), True)

        self.assertEqual(abs(v) == sqrt(1 + 4**2 + 9 + 16), False)

        self.assertEqual(abs(v + c), sqrt(25 + 25 + 25 + 25))

    def test_ndim(self):
        v = self._get_vector()
        c = Vector([4, 3, 2, 1])

        self.assertEqual(v.ndim() == c.ndim(), True)

        self.assertEqual(v.ndim() == (c + v).ndim(), True)

        c.append(5)
        self.assertEqual(v.ndim() == c.ndim(), False)

    def test_clear(self):
        v = self._get_vector()
        c = Vector([4, 3, 2, 1])

        self.assertNotEqual(v == [], True)

        v.clear()
        self.assertEqual(v == [], True)

        c.clear()
        self.assertEqual(v, c)

    def test_getitem(self):
        v = self._get_vector()

        self.assertNotEqual(v[0] == 0, True)

        c = Vector([1, 3, 2, 1])
        self.assertEqual(c[0], c[3])

        with self.assertRaises(IndexError):
            print(c[5])

    def test_setitem(self):
        v = self._get_vector()
        v[3] = 1
        self.assertEqual(v[0], v[3])

        c = Vector([1, 3, 2, 1])
        c[0] = 3
        self.assertEqual(c[0], v[2])

        with self.assertRaises(IndexError):
            c[6] = 2

    def test_reverse(self):
        v = self._get_vector()
        c = Vector([4, 3, 2, 1])

        c.reverse()
        self.assertEqual(v, c)

        s = [1, 2, 1]
        s1 = [1, 2, 1]
        s1.reverse()
        self.assertEqual(s, s1)

    def test_argmax(self):
        v = self._get_vector()
        c = Vector([4, 3, 2, 1])

        self.assertEqual(c.argmax(), 0)

        self.assertEqual(c[v.argmax()], 1)

        self.assertNotEqual(c.argmax(), v.argmax())

    def test_argmin(self):
        v = self._get_vector()
        c = Vector([4, 3, 2, 1])

        self.assertEqual(c.argmin(), v.argmax())

        self.assertEqual(v.argmin(), 0)

        self.assertEqual(c.argmin(), 3)

    def test_eq(self):
        p = self._get_vector()
        v = Vector([1, 2, 3, 4])

        self.assertEqual(p, v)

        v.append(5)
        self.assertEqual(Vector([1, 2, 3, 4, 5]), v)

        self.assertNotEqual(p, repr(p))


if __name__ == "__main__":
    unittest.main()
