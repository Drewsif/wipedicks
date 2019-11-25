#!/usr/bin/env python
from __future__ import print_function, unicode_literals
import os
import threading
import random
try:
    random = random.SystemRandom()
except:
    print('Using built in random number generator...')

# This was generated using generate_dick_list()
DICKS = ['8=D ', '8=D~ ', '8=D~~ ', '8=D~~~ ', '8==D ', '8==D~ ', '8==D~~ ', '8==D~~~ ', '8===D ', '8===D~ ', '8===D~~ ', '8===D~~~ ', '8====D ', '8====D~ ', '8====D~~ ', '8====D~~~ ', '8=====D ', '8=====D~ ', '8=====D~~ ', '8=====D~~~ ', '8======D ', '8======D~ ', '8======D~~ ', '8======D~~~ ', '8=======D ', '8=======D~ ', '8=======D~~ ', '8=======D~~~ ', '8========D ', '8========D~ ', '8========D~~ ', '8========D~~~ ', '8=========D ', '8=========D~ ', '8=========D~~ ', '8=========D~~~ ', '8==========D ', '8==========D~ ', '8==========D~~ ', '8==========D~~~ ', '8===========D ', '8===========D~ ', '8===========D~~ ', '8===========D~~~ ', '8============D ', '8============D~ ', '8============D~~ ', '8============D~~~ ', '8#=D ', '8#=D~ ', '8#=D~~ ', '8#=D~~~ ', '8#==D ', '8#==D~ ', '8#==D~~ ', '8#==D~~~ ', '8#===D ', '8#===D~ ', '8#===D~~ ', '8#===D~~~ ', '8#====D ', '8#====D~ ', '8#====D~~ ', '8#====D~~~ ', '8#=====D ', '8#=====D~ ', '8#=====D~~ ', '8#=====D~~~ ', '8#======D ', '8#======D~ ', '8#======D~~ ', '8#======D~~~ ', '8#=======D ', '8#=======D~ ', '8#=======D~~ ', '8#=======D~~~ ', '8#========D ', '8#========D~ ', '8#========D~~ ', '8#========D~~~ ', '8#=========D ', '8#=========D~ ', '8#=========D~~ ', '8#=========D~~~ ', '8#==========D ', '8#==========D~ ', '8#==========D~~ ', '8#==========D~~~ ', '8#===========D ', '8#===========D~ ', '8#===========D~~ ', '8#===========D~~~ ', '8#============D ', '8#============D~ ', '8#============D~~ ', '8#============D~~~ ']
_fast_cache = ''
_cache_count = 0


def generate_dick_list():
    dicks = []
    for a in range(0, 2):
        for b in range(1, 13):
            for c in range(0, 4):
                dick = '8'
                dick += '#' * a
                dick += '=' * b
                dick += 'D' + '~' * c
                dick += ' '
                dicks.append(dick)
    return dicks


def rand_dick():
    return random.choice(DICKS)


def fast_rand_dick():
    global _fast_cache
    global _cache_count
    if not _fast_cache or not _cache_count:
        _fast_cache = ''
        _cache_count = random.randint(1000, 10000)
        for _ in range(0, random.randint(150, 300)):
            _fast_cache += random.choice(DICKS)
    _cache_count -= 1
    return _fast_cache


def wipe(dev, rounds=1):
    try:
        size = os.path.getsize(dev)
    except:
        size = 0

    if size == 0:
        for i in range(0, rounds):
            try:
                f = open(dev, 'w')
            except Exception as e:
                print('ERROR:', dev, e)
                return False

            while True:
                try:
                    f.write(rand_dick())
                except IOError:
                    f.close()
                    break
    else:
        for i in range(0, rounds):
            try:
                f = open(dev, 'w')
            except Exception as e:
                print('ERROR:', dev, e)
                return False

            dlen = 0
            while dlen < size:
                dick = rand_dick()
                dlen += len(dick)
                try:
                    f.write(dick)
                except IOError:
                    f.close()
                    break

        dlen = 0
        dick = ''
        while dlen < len(dev):
            dick += rand_dick()
            dlen += len(dick)
        try:
            os.rename(dev, dick)
            dev = dick
        except:
            pass

        os.remove(dev)

    return True


def parse_dir(directory, recursive=False):
    """
    Returns a list of files in a directory.

    dir - The directory to search
    recursive - If true it will recursively find files.
    """
    filelist = []
    for item in os.listdir(directory):
        item = os.path.join(directory, item)
        if os.path.isdir(item):
            if recursive:
                filelist.extend(parse_dir(item, recursive))
            else:
                continue
        else:
            filelist.append(item)
    return filelist


def parse_filelist(FileList, recursive=False):
    """
    Takes a list of files and directories and returns a list of files.

    FileList - A list of files and directories. Files in each directory will be returned
    recursive - If true it will recursively find files in directories.
    """
    filelist = []
    for item in FileList:
        if os.path.isdir(item):
            if recursive:
                filelist.extend(parse_dir(item, recursive))
            else:
                print('WARNING:', item, 'is a directory and recursive is off.')
        elif os.path.exists(item):
            filelist.append(item)
        else:
            pass
    return filelist


def _main():
    import argparse
    parser = argparse.ArgumentParser(description="Wipe files/devices with dicks")
    parser.add_argument("-r", "--recursive", action="store_true", help="Recursively parse folders for files to wipe")
    parser.add_argument('-n', '--numrounds', help="The number of rounds to write the files", required=False, metavar="num", default=1, type=int)
    parser.add_argument("-w", "--wipefree", action="store_true", help="Wipe the free space by creating a large file")
    parser.add_argument("-s", "--slow", action="store_true", help="Use more randomness, tends to be slower")
    parser.add_argument('Files', help="Files, Directories, and Devices to wipe", nargs='+')
    args = parser.parse_args()

    if not args.slow:
        global rand_dick
        rand_dick = fast_rand_dick

    file_list = parse_filelist(args.Files)
    thread_list = []
    kwargs = {'rounds': args.numrounds}
    if args.wipefree:
        file_list.append('dick.tmp')
    for f in file_list:
        t = threading.Thread(target=wipe, args=(f,), kwargs=kwargs)
        t.daemon = True
        t.start()
        thread_list.append(t)

    for t in thread_list:
        t.join()


if __name__ == '__main__':
    _main()
