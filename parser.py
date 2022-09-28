import os
from base_lib import base_lib
from lexer import lexer
from useful_stuff import uo

class parser_stage1:
    def __init__(self, fpath):
        self.fpath = fpath
    def initial_reading(self):
        self.file = open(self.fpath, "r")
    def lineskimmer(self):
        line = 0
        for f in self.file:
            line += 1 # increment line number
            # print(str(f.split("=")[0]))
            if str(f).isspace():
                pass
            elif str(f).find("#") == 0:
                pass
            elif "=" in f and "\"" not in f.split("=")[0] and not "=>" in f: 
                #print(f)
                lexer.variable_name_verify(f, line)
                lexer.variable_assign(f, line)
            elif f.count('"') - f.count('\\"') == 2 and f.find('"') == 0:
                base_lib.stdout(f)
            elif f.count("=>") == 1:
                lexer.lambda_fn(f)
            else:
                uo.Error(f"Invalid syntax on line {line}.")
                exit()
        exit()
    
                


        
        
