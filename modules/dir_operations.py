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
    print(func,": invalid option -- \'"+opt+'\'')

def ls(opts,args):
    for opt in opts:
        if not ((opt == 'R') or (opt == 'recursive')):
            inv_opt(ls.__name__,opt)
            return

    for arg in args:
        path = os.path.join(os.getcwd(),str(arg))
        if not (os.path.isfile(path) or os.path.isdir(path)):
            print("ls: cannot access \'",arg,"\': No such file or directory")
            return
        if ('R' in opts) or ('recursive' in opts):
            queue = []
            queue.append(arg)
            while( len(queue) > 0):
                parent = queue.pop(0)
                print(('.'+parent+":\n"))
                files = [f for f in os.listdir(os.path.join(os.getcwd(),parent)) if f[0] != '.']
                for file in files:
                    if os.path.isdir(os.path.join(parent,file)):
                        queue.append(os.path.join(parent,file))
                    print(file,"  ",end ="")
                print('\n')
        else:
            if(len(args) > 1):
                print(arg," :\n")
            files = [f for f in os.listdir(os.path.join(os.getcwd(),arg)) if f[0] != '.']
            for file in files:
                print(file,"  ",end ="")
            print('\n')

def cd(opts,args):
    
    if(len(args)>1):
        print(cd.__name__,": too many arguments")
        return

    if( len(opts)>0 ):
        inv_opt(cd.__name__,opts[0])
        return

    if os.path.isdir(str(args[0])):
        os.chdir(str(args[0]))
    else:
        print(cd.__name__,": ",args[0],": No such file or directory")

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