#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from flatten import Flatten


class TestFlatten(unittest.TestCase):

    def test_flatten_01(self):
        f = Flatten()
        res = f.flatten([1, 2, [4, 5]])
        self.assertEqual(res, [1, 2, 4, 5])

    def test_flatten_02(self):
        f = Flatten()
        res = f.flatten([1, 2, [4, 5], 6, [7, 8, [[9]]]])
        self.assertEqual(res, [1, 2, 4, 5, 6, 7, 8, 9])


if __name__ == '__main__':
    unittest.main()