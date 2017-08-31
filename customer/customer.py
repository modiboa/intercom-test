#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json


class Customer(object):

    def __init__(self, user_id, name, latitude, longitude):
        self.user_id = user_id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    @staticmethod
    def from_json(json_string):
        json_obj = json.loads(json_string)
        return Customer(json_obj['user_id'], json_obj['name'], json_obj['latitude'], json_obj['longitude'])
