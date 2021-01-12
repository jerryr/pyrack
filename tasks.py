from invoke import task

from cffi import FFI
import pathlib

@task
def gencffi(c):
    """ Build the CFFI Python bindings """
    #print_banner("Building CFFI Module")
    ffi = FFI()
    this_dir = pathlib.Path().absolute()
    h_file_name = this_dir / "ladspa.h"
    with open(h_file_name) as h_file:
        ffi.cdef(h_file.read())
    ffi.set_source(
        "ladspa_api",
        None
    )

    ffi.compile()

