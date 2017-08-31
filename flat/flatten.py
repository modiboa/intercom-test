#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""flatten an array of nested arrays of integers into a flat array of integers """

class Flatten(object):

	def flatten(self, arr):
	    if arr == []:
	        return arr
	    if isinstance(arr[0], list):
	        return self.flatten(arr[0]) + self.flatten(arr[1:])
	    return arr[:1] + self.flatten(arr[1:])
