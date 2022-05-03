"""
Python version of this:
https://github.com/sindresorhus/safe-stringify/blob/main/index.js
"""

import json


def _make_circular_ref(obj):
	global obj
	
	if obj and isinstance(obj, (tuple, list)):
		return _replacer_arr(obj)

	if obj and isinstance(obj, dict):
		return _replacer_obj(obj)

	return obj


def _replacer_arr(array):
	res = []
	for item in array:
		if item is obj:
			res.append('Cyclic Ref')
		elif isinstance(item, (tuple, list)):
			res.append(_replacer_arr(item))
		elif isinstance(item, dict):
			res.append(_replacer_obj(item))
		else:
			res.append(item)
	return res

def _replacer_obj(object):
	res = {}
	for key in object:
		if object[key] is obj:
			res[key] = 'Cyclic Ref'
		elif isinstance(object[key], (tuple,list)):
			res[key] = _replacer_arr(object[key])
		elif isinstance(object[key], dict):
			res[key] = _replacer_obj(object[key])
		else:
			res[key] = object[key]
	return res

def safejson(collection):
	print(collection)
	return _make_circular_ref(collection)


"""
1. get passed obj: (list, tuple, or dict container)
1a. if obj is not in the type list above; return as is.
2. if obj type is list or tuple, initialize an empty
list container
3. if obj type is dict, initialize an empty dict
container
4. Iterate through obj recursively
5. 
"""