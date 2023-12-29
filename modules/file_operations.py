"""
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
"""
import os
import shutil
import re
from utils import inv_opt


def find(opts, args):
    if len(opts) > 0:
        inv_opt(find.__name__, opts[0])
        return

    files = [f for f in os.listdir() if f[0] != '.']
    for arg in args:
        if arg in files:
            if os.path.isfile(arg):
                print(arg)
            queue = []
            queue.append(arg)
            if os.path.isdir(arg):
                while len(queue) > 0:
                    file_path = queue.pop()
                    print(file_path)
                    if os.path.isdir(file_path):
                        queue = queue + [file_path + '/' + f for f in os.listdir(file_path)]
        else:
            print(find.__name__, '\'' + arg + '\'', ': No such file or directory exists in this folder')


def sizeof(opts, args):
    if len(opts) > 0:
        inv_opt(sizeof.__name__, opts[0])
        return

    for arg in args:
        file_path = os.path.join(os.getcwd(), arg)
        if not (os.path.isfile(file_path)) or os.path.isdir(file_path):
            print(sizeof.__name__ + ":", arg + ": is not a File or is a Directory")
            continue
        size = os.lstat(file_path)[6]
        ext = "B"
        if size > 1000:
            size = size / 1000
            ext = "kB"
        if size > 1000:
            size = size / 1000
            ext = "MB"
        print("Size of", arg + ": ", size, ext)
    return


def tail(opts, args):
    if len(opts) > 0:
        inv_opt(tail.__name__, opts[0])
        return

    for arg in args:

        file_path = os.path.join(os.getcwd(), arg)

        if os.path.isdir(file_path):
            print(tail.__name__ + ": error reading '" + arg + "': Is a directory")
            continue

        elif not os.path.isfile(file_path):
            print(tail.__name__ + ": cannot open '" + arg + "': No such file exists")
            continue

        f = open(file_path, 'r')
        lines = f.readlines()
        f.close()
        if len(args) > 1:
            print("==>", arg, "<==")

        if len(lines) >= 10:
            start = -10
        else:
            start = -1 * (len(lines))

        while start <= -1:
            print(lines[start], end="")
            start = start + 1
            if (start == 0) and (arg != args[len(args) - 1]):
                print()


def head(opts, args):
    if len(opts) > 0:
        inv_opt(head.__name__, opts[0])
        return
    for arg in args:

        file_path = os.path.join(os.getcwd(), arg)

        if os.path.isdir(file_path):
            print(head.__name__ + ": error reading '" + arg + "': Is a directory")
            continue

        elif not os.path.isfile(file_path):
            print(head.__name__ + ": cannot open '" + arg + "': No such file exists")
            continue

        f = open(file_path, 'r')
        lines = f.readlines()
        f.close()
        if len(args) > 1:
            print("==>", arg, "<==")
        for i in range(len(lines)):
            if i == 10:
                if arg != args[len(args) - 1]:
                    print()
                break
            print(lines[i][:-1])
    return


def grep(opts, args):
    if len(opts) > 0:
        inv_opt(grep.__name__, opts[0])
        return
    if len(args) < 1:
        print("At least 2 arguments are needed")
    pattern = args[0]
    for i in range(len(args) - 1):
        file_path = os.path.join(os.getcwd(), args[i + 1])
        if not os.path.isfile(file_path):
            print(grep.__name__ + ":", args[i + 1] + ":", "No Such file exists.")
            continue
        if os.path.isdir(file_path):
            print(grep.__name__ + ":", args[i + 1] + ":", "Is a directory.")
            continue
        files = open(file_path, 'r')
        lines = files.readlines()
        files.close()
        for line in lines:
            if len(re.findall(pattern, line)):
                if len(args) > 2:
                    print(args[i + 1] + ":", end=" ")
                print(line[1:len(line) - 2])
    return


def mv(opts, args):
    if len(opts) > 0:
        inv_opt(mv.__name__, opts[0])

    if len(args) != 2:
        print("Arguments should be 2")
        return

    file_path = os.path.join(os.getcwd(), args[0])

    dest_path = os.path.join(os.getcwd(), args[1])

    if os.path.isdir(dest_path):
        args[1] = args[1] + '/'

    shutil.move(file_path, dest_path)


def rm(opts, args):
    is_r = False
    for opt in opts:
        if opt != 'r':
            inv_opt(rm.__name__, opt)
            return
        elif opt == 'r':
            is_r = True

    for arg in args:
        file_path = os.path.join(os.getcwd(), arg)

        if not os.path.exists(file_path):
            print(rm.__name__, ": cannot remove \'", arg, "\': No such file or directory exists")
            continue

        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            try:
                os.rmdir(file_path)
            except:
                if is_r:
                    shutil.rmtree(file_path)
                else:
                    print(rm.__name__, ': cannot remove', arg, "Is a directory")
                    continue


def cp(opts, args):
    if len(opts) > 0:
        inv_opt(cp.__name__, opts[0])
        return

    if len(args) < 2:
        print("Missing min. number of arguments")
        return

    dest_path = os.path.join(os.getcwd(), args[-1])
    if len(args) > 2 and not os.path.isdir(dest_path):
        print(cp.__name__, "target", args[-1], "is not a directory or doesn't exist")
        return

    for i in range(len(args) - 1):
        file_path = os.path.join(os.getcwd(), args[i])
        if not (os.path.exists(file_path)) or os.path.isdir(file_path):
            print(args[i], "doesn't exist or is a directory")
            return
        if len(args) == 2:
            dest_path = os.path.join(os.getcwd(), args[1])
        else:
            dest_path = os.path.join(os.getcwd(), os.path.join(args[-1], args[i]))
        shutil.copyfile(file_path, dest_path)


def cat(opts, args):
    if len(args) == 1 and args[0] == '':
        while 1:
            try:
                str = input()
                print(str)
            except:
                return

    if len(opts) > 0:
        inv_opt(cat.__name__, opts[0])
        return
    else:
        to_write = []
        for i in range(len(args)):
            if args[i][0] == '>':
                to_write = to_write + [i]
        if len(to_write) > 0 and to_write[-1] == len(args) - 1:
            f = open(args[-1][1:], 'w')
            while 1:
                try:
                    str = input()
                    f.write(str)
                    f.write('\n')
                except:
                    f.close()
                    break

        elif len(to_write) > 0 and to_write[-1] != len(args) - 1:
            return

        elif len(to_write) == 0:
            for arg in args:
                try:
                    f = open(arg, 'r')
                except FileNotFoundError:
                    print("No such file or directory:", arg)
                    return
                strs = f.readlines()
                for str in strs:
                    print(str, end="")
