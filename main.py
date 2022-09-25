from argument_handler import init_args 
from useful_stuff import uo
from parser import parser_stage1
import os
from os import sys



def main():
    fpath = ""
    if (len(sys.argv) < 2):
        uo.Error("No filepath supplied")
        exit()
    


    ## ARGUMENT PHASE
    fpath = sys.argv[1].strip()
    if (fpath == "-v" or fpath == "--version"):
        return print(f"Argo Navis version \033[35m{uo.Version()}\033[0m")
    #print(fpath)
    init_args.test_is_allowed(fpath)

    ##PREREQUISITES TO PARSER PHASE
    fstr_cache = open(".argo_cache", "w")
    #fstr_cache.write(f"# DON'T EDIT THIS FILE. (Argo Navis version {uo.Version()})\n\n")
    fstr_cache.close()

    ##PARSER PHASE
    parser = parser_stage1(fpath)
    parser.initial_reading()
    parser.lineskimmer()


main()