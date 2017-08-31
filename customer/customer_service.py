#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from math import sin, asin, cos, sqrt, atan2, radians
from customer import Customer


class CustomerService(object):

    DUBLIN_LAT = 53.3393
    DUBLIN_LON = -6.2576841

    def calculate_distance(self, lon1, lat1):

        # convert decimal degrees to radians 
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, self.DUBLIN_LON, self.DUBLIN_LAT])

        dlon = lon2 - lon1 
        dlat = lat2 - lat1 
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * asin(sqrt(a)) 
        km = 6367 * c
        return km

    def get_near_customers(self):       
        near_customers = []
        with open('customer.json') as f:
            for line in f:
                customer = Customer.from_json(line);
                distance = self.calculate_distance(float(customer.longitude), float(customer.latitude))
                if distance <= 100:
                    near_cust = {'user_id': customer.user_id, 'name': customer.name}
                    near_customers.append(near_cust)

        sorted_list = sorted(near_customers, key=lambda customer: customer['user_id'])
        return sorted_list

    def check_customers(self):
        try:
            customer_list = self.get_near_customers()
            for cust in customer_list:
                print('Id: ' + str(cust['user_id']) + '    Name: ' + cust['name'])
        except IOError:
            print("Can't open customers file")




if __name__ == '__main__':
    cs = CustomerService()
    cs.check_customers()