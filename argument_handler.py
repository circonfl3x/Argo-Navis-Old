from os import sys
import os
from useful_stuff import uo

class init_args:
    def __init__(self,fpath):
        self.path = fpath
    
    def test_is_allowed(path):
        if(os.path.exists(path)):
            pass
        else:
            uo.Error(f"{path} doesn't exist in filesystem")
            exit()
