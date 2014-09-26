#!/usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = "José Carrasco"
# __status__ = "Production"

import json, datetime, decimal

def as_json(model):
    _json = {}
    for col in model._sa_class_manager.mapper.mapped_table.columns:
            _json[col.name] = getattr(model, col.name)
    return _json

def str_complex_type(value):
    if type(value) in (int, float, long, bool):
        return str(value)
    elif type(value) is unicode:
        return value.encode('utf-8')
    elif isinstance(value, datetime.date) \
        or isinstance(value, datetime.time) \
            or isinstance(value, datetime.datetime):
        return value.isoformat()
    elif  isinstance(value, decimal.Decimal):
        return str(value)
    return value

def as_json_dump(model, default=None):
    if not default:
        default = str_complex_type
    return json.dumps(as_json(model), default=default)

def json_dump(model, default=None):
    if not default:
        default = str_complex_type
    return json.dumps(model,default=default)
