#!/usr/bin/env python

import pathlib
import os
from ladspa_api import ffi

if __name__ == "__main__":
    ladspa_path = os.environ["LADSPA_PATH"]
    libname = "tap_tremolo.so"
    path = pathlib.Path(ladspa_path) / libname 
    lib = ffi.dlopen(str(path))
    plugin = lib.ladspa_descriptor(0)

    print("Plugin Name: %s\n" % ffi.string(plugin.Name))
    print("Label: %s\n" % ffi.string(plugin.Label))

    port_count = plugin.PortCount
    ports = plugin.PortNames
    for i in range(0, port_count):
        # Find the input control ports
        if(plugin.PortDescriptors[i] == lib.LADSPA_PORT_CONTROL | lib.LADSPA_PORT_INPUT):
            name = ports[i]
            print(ffi.string(name))

