#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from customer_service import CustomerService


class TestCustomerService(unittest.TestCase):

    def test_calculate_distance(self):
        cs = CustomerService()
        self.assertEqual(int(cs.calculate_distance(-0.155163, 51.515314)), 460)

if __name__ == '__main__':
    unittest.main()


