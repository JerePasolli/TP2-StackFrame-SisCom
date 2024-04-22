from msl.loadlib import Server32
import ctypes

class MyServer(Server32):
    """Wrapper around a 32-bit C++ library 'my_lib.dll' that has an 'add' and 'version' function."""

    def __init__(self, host, port, **kwargs):
        # Load the 'my_lib' shared-library file using ctypes.CDLL
        super(MyServer, self).__init__('lib/libaddToGINI.so', 'cdll', host, port)

        # The Server32 class has a 'lib' property that is a reference to the ctypes.CDLL object

        # Call the version function from the library
        self.lib.add_one.restype = ctypes.c_int
        self.lib.add_one.argtypes = [ctypes.c_float]
        # self.version = self.lib.version()

    def add_one(self, n):
        # The shared library's 'add' function takes two integers as inputs and returns the sum
        return self.lib.add_one(n)