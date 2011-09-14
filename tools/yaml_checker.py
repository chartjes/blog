#!/usr/bin/env python
import getopt
import os
import re
import sys
import yaml

from yaml import load, dump

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):
    if argv is None:
        argv = sys.argv

    try:
        try:
            print "Checking markdown files in the current directory..."

            #root = "/Users/chartjes/Documents/atthekeyboard/source/_posts"
            for r,d,f in os.walk('.'):
                for file in f:
                    fp = open(file, 'r') 
                    contents = fp.read()
                    marker = "---"
                    a = contents.find(marker)
                    b = contents.find(marker, a + len(marker))
                    try:
                        yaml_to_parse = contents[a:b]
                        yaml.load(yaml_to_parse)
                    except:
                        print "%s is invalid YAML" % file
        except getopt.error.msg:
            raise Usage(msg)
    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2

if __name__ == "__main__":
    sys.exit(main())
