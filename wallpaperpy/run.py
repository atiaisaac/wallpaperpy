from __future__ import print_function
from __future__ import absolute_import
from . import envs
import os
import sys
import time
import optparse




def display(path,delay):
    try:
        while True:
            for r,d,f in os.walk(path):
                for i in f:
                    envs.set_background(os.path.join(path,i))
                    time.sleep(delay)
    except Exception:
        print ("[-] Cannot execute")
        raise


def main():
    parser=optparse.OptionParser("usage: %prog -p <absoulte path> -s <time delay>")
    parser.add_option("-p","--path",dest="path",type="string",help="Specify absolute path to images folder")
    parser.add_option("-s","--sleep",dest="delay",type="int",help="sleep time between images as it changes")
    (options,args)=parser.parse_args()
    path=options.path
    delay=options.delay
    if (path==None) | (delay==None):
        print (parser.usage)
        sys.exit(0)
    display(path,delay)


if __name__=="__main__":
    main()
