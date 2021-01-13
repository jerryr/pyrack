#!/usr/bin/env python

import pathlib
import os
from ladspa_api import ffi

def decode_string(s):
    return ffi.string(s).decode("utf-8")

def list_ladspa_plugins():
    ladspa_path = pathlib.Path(os.environ["LADSPA_PATH"])
    files = ladspa_path.glob("*.so")
    plugins = []
    for f in files:
        plugindef = {}
        lib = ffi.dlopen(str(f))
        plugin = lib.ladspa_descriptor(0)
        plugindef["name"] = decode_string(plugin.Name) 
        plugindef["label"] = decode_string(plugin.Label) 

        portdef = []
        port_count = plugin.PortCount
        ports = plugin.PortNames
        for i in range(0, port_count):
            # Find the input control ports
            if(plugin.PortDescriptors[i] == lib.LADSPA_PORT_CONTROL | lib.LADSPA_PORT_INPUT):
                name = ports[i]
                portdef.append(decode_string(name))
        plugindef["ports"] = portdef
        plugins.append(plugindef)
    return {"plugins": plugins}


if __name__ == "__main__":
    plugins = list_ladspa_plugins()
    print(plugins)

