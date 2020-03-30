import os
import sys
from modules import file_operations,dir_operations
from utils import *
# step 1
# Prepare command parser: identify command and arguments
#directory/file related commands must be implemented as a separate module
#Thus, to add a new command into the shell, create a python module with the same name as 
# the command in a specific folder. 
# This module should have run() function that would contain the command implementation.
# step 2
# log commands in history data base
# step 3
# switch to appropriate function depending on cmd (modular/scalable approach)
# step 4
# The interface for adding new custom commands must be simple.
# step 5
# figure out a way to package this

def print_command(cmd,opts,args):
    print("command   : ",cmd)
    print("Options   : ", opts)
    print("Arguments : ",args)


def py():
    print("pyshell>>", end=" ")    

def imports():
    module_path = os.path.join(os.getcwd(),'modules')
    modules = [f[:-3] for f in os.listdir(module_path) if os.path.isfile(os.path.join(module_path,f))]
    return modules

def str_to_class(str):
    return getattr(sys.modules[__name__],str)


if __name__ == "__main__":
    #CORE EVENT LOOP
    version = "v0.001"
    hf_path,count = initalize_history() 
    modules = imports()
    #print(modules)
    debug = 0
    print("Welcome to pyshell",version)
    try:
        while(1):
            py()
            ori_cmd = input()
            opts = []
            args = []
            cmd, opts, args = pre_process_cmd(ori_cmd)
            if(debug):
                print_command(cmd,opts,args)

            for module in modules:
                if(debug):
                    print("Searchin in :",module)
                try:
                    function = getattr(str_to_class(module),cmd)
                    if(debug):
                        print("Found function : ",function," in :",module)
                    break
                except AttributeError:
                    pass

            try:
                if(debug):
                    print("Running : ",function)
                function(opts,args)
                count = log_cmd(ori_cmd,hf_path,count)
                del(function)
            except NameError:
                print("Command not found")
    except KeyboardInterrupt:
        print("\nThanks for using pyshell",version)
        print("Closing...")        