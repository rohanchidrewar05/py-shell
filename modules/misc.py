#    Miscellaneous commands:
#    date (built-in command)
#    whoami (built-in command)
#    hostname (built-in command)
#    timeit (built-in command - print time taken by a command in seconds)
#    exit (built-in command)
#    history (built-in command)

from utils import inv_opt
import time
from modules import dir_operations 
from main import get_function,run_function
from utils import  initalize_history

def timeit(opts,args):
    debug = 1
    tic = time.time()
    if len(args) > 0:
        cmd = args[0]

    if len(args) == 1:
        args = ['']
    else:
        args = args[1:]

    function = get_function(cmd,debug)
    _ = run_function(function,opts,args,debug)
    toc = time.time()
    print("Time taken by \'"+cmd+'\'',str(toc-tic),'secs')

def exit(opts,args):
    
    if(len(opts)>0):
        inv_opt(exit.__name__,opts[0])
        return

    if(len(args)>1 or args[0]!=''):
        print(args[0]+':',"the term is not recognized")
        return

    raise(KeyboardInterrupt)

def history(opts,args):
    lines_to_get = 500
    if len(opts)>0:
        inv_opt(history.__name__,opts[0])
        return

    if len(args) == 1 and args[0] != '':
        try:
            lines_to_get = int(args[0])
        except ValueError:
            print("Invalid option, it should be interger")
            return
    try:
        file = open('logs/history.txt','r')
    except FileNotFoundError:
        dir_operations.mkdir([],['logs'])
        file = open('logs/history.txt','w')
        file.close()
        file = open('logs/history.txt','r')

    lines = file.readlines()
    file.close()
    total_lines = len(lines)
    lines_to_get = min(lines_to_get,total_lines)
    start_index = max(0,total_lines-lines_to_get)
    for i in range(lines_to_get):
        print(lines[start_index+i],end='')
    return