#!/usr/bin/env python
from bottle import route, run, template
import ladspa_info

@route('/plugins/list')
def list():
    return ladspa_info.list_ladspa_plugins()

run(host='localhost', port=8080)