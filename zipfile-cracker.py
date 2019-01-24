#!/usr/bin/env python
import zipfile
from threading import Thread
import optparse

def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        print("[+] Found password " + password + "\n")
        print 'Congratulations...Your file has been extracted!'
    except:
        pass
def main():
    parser = optparse.OptionParser("program usage: " +\
                                   "-f <zipfile> -d <dictionary>")
    parser.add_option("-f", dest="zname",\
                      help="Please specify a zip file")
    parser.add_option("-d", dest="dname",\
                      help="Please specify a dictionary file")
    (options, args) = parser.parse_args()
    if (options.zname == None) | (options.dname == None):
        print(parser.usage)
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
    zFile = zipfile.ZipFile(zname)
    passFile = open(dname)
    for line in passFile.readlines():
        password = line.strip("\n")
        t = Thread(target=extractFile, args=(zFile, password))
        t.start()
if __name__ == '__main__':
    main()