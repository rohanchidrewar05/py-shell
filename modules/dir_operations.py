'''
ls (with support for -R or --recursive switch for listing contents of directory recursively)
mkdir
pwd
rmdir
cd
'''
import os
import shutil

def inv_opt(func,opt):
    print(func,": invalid option -- \'",opt,'\'')

def pwd(opts,args):
    if( len(opts)>0 ):
        inv_opt(pwd.__name__,opts[0])
        return
    print(os.getcwd())

def mkdir(opts,args):
    if( len(opts)>0 ):
        inv_opt(mkdir.__name__,opts[0])
        return

    rnw = "str"
    try:
        for arg in args:
            rnw = str(arg)
            os.mkdir(rnw)
    except FileExistsError:
        print('\'',rnw,'\'',"already exists")

def rmdir(opts,args):
    rnw = "str"
    try:
        for arg in args:
            rnw = str(arg)
            os.rmdir(rnw)
    
    except OSError:
        if( len(opts) == 0 or ('r' not in opts)):
            print("Directory not empty")
            return

        for opt in opts:
            if opt != 'r':
                inv_opt(rmdir.__name__,opt)
                return
        for arg in args:
            rnw = str(arg)
            shutil.rmtree(rnw)