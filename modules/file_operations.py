'''
* File related commands:
    cat
    cp
    rm (with support for -r switch to recursively delete folder/files)
    mv
    grep
    head
    tail
    sizeof (print size of a file in bytes)
    find
'''
import os

def inv_opt(func,opt):
    print(func,": invalid option -- \'"+opt+'\'')

def cat(opts,args):
    if len(args) == 1 and args[0]=='':
        while(1):
            try:
                str = input()
                print(str)
            except:
                return
                
    if len(opts)>0:
        inv_opt(cat.__name__,opts[0])
        return
    else:
        to_write = []
        for i in range(len(args)):
            if args[i][0] == '>':
                to_write = to_write + [i]
        if len(to_write) > 0 and to_write[-1] == len(args)-1:
            f = open(args[-1][1:],'w')
            while(1):
                try:
                    str = input()
                    f.write(str)
                    f.write('\n')
                except:
                    f.close()
                    break

        elif len(to_write) > 0 and to_write[-1] != len(args)-1:
            return
        
        elif len(to_write) == 0:
            for arg in args:
                try:
                    f = open(arg,'r')
                except FileNotFoundError:
                    print("No such file or directory:",arg)
                    return
                strs = f.readlines()
                for str in strs:
                    print(str, end="")

def cp(opts,args):
    pass