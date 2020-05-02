
import re
import os

def inv_opt(func,opt):
    print(func,": invalid option -- \'"+opt+'\'')

def log_cmd(str,hf_path,count):
    if(count < 1000):
        hf = open(hf_path,'r+')
        hf.seek(0,2)
        hf.write(str)
        hf.write("\n")
        count = count + 1
        hf.close()
    else:
        hf = open(hf_path,'r')
        lines = hf.readlines()
        hf.close()
        hf = open(hf_path,'w')
        for i in range(len(lines)-1):
            hf.write(lines[i+1])
        hf.write(str)
        hf.write("\n")
        hf.close()
    return count

def pre_process_cmd(str):
    
    sm_temp_opts = re.findall(' -\w+',str)
    sm_temp_opts = [f[1:] for f in sm_temp_opts]
    small_opts = []
    for opt in sm_temp_opts:
        small_opts = small_opts + [opt[1:]]

    bg_temp_opts = re.findall(' --\w+',str)
    bg_temp_opts = [f[1:] for f in bg_temp_opts]
    big_opts = []
    for opt in bg_temp_opts:
        big_opts = big_opts + [opt[2:]]
 
    opts = []
    for opt in small_opts:
        opts = opts + list(opt) 
    opts = opts + big_opts

    words = str.split(" ")
    cmd = words[0]
    
    args = []
    for word in words:
        if word not in sm_temp_opts+bg_temp_opts+[cmd]:
            args = args+[word]
    if len(args)==0:
        args = ['']
    
    return cmd,opts,args

def initalize_history():
    hf_path = os.path.join(os.path.join(os.getcwd(),'logs'),'history.txt')
    hf = open(hf_path,'r+')
    count = 0
    for line in hf:
        count = count + 1
    hf.close()
    return hf_path,count