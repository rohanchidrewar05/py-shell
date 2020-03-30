import re
import os

def log_cmd(str,hf_path,count):
    if(count < 200):
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
    pattern = re.compile('-\w+')
    temp_opts = re.findall(pattern,str)
    big_opts = re.findall('--\w+',str)
    #print(temp_opts)
    #print(big_opts)
    opts = []
    for opt in temp_opts:
        if '-'+opt not in big_opts:
            i = 1
            while(i<len(opt)):
                opts = opts + list(opt[i]) 
                i = i + 1
    
    opts = opts + [ big[2:] for big in big_opts]
    ending = 0
    for match in re.finditer(pattern,str):
        ending = match.end()+1
    
    cmd = str.split(" ")[0]
    if(ending == 0):
        ending = len(cmd)+1
    args = str[ending:].split(' ')
    return cmd,opts,args

def initalize_history():
    hf_path = os.path.join(os.path.join(os.getcwd(),'utils'),'history.txt')
    hf = open(hf_path,'r+')
    count = 0
    for line in hf:
        count = count + 1
    hf.close()
    return hf_path,count