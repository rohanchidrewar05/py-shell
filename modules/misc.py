from utils import inv_opt

'''
* Miscellaneous commands:
    date (built-in command)
    whoami (built-in command)
    hostname (built-in command)
    timeit (built-in command - print time taken by a command in seconds)
    exit (built-in command)
    history (built-in command)
'''

def exit(opts,args):
    
    if(len(opts)>0):
        inv_opt(exit.__name__,opts[0])
        return

    if(len(args)>1 or args[0]!=''):
        print(args[0]+':',"the term is not recognized")
        return
    
    raise(KeyboardInterrupt)