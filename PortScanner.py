import sys
from socket import *
from threading import *



print '\t\t\t ######################################'
print '\t\t\t ##                                  ##'
print '\t\t\t ##   Author : Sandeep Saini         ##'
print '\t\t\t ######################################'


def threadScan(site,port) :
    scan = socket(AF_INET, SOCK_STREAM)
    connect = scan.connect_ex((site, port))
    if (connect == 0) :
        print  "[+]\tPort",port,": Open"
    else : 
        print "[-]\tPort",port,": Close" 
    scan.close()
    
site = raw_input("Enter WebSite {www.target.com}: ")
ports = raw_input("Enter Ports {21,22,80,....} : ")
port = str(ports).split(',')
ip = gethostbyname(site)
print '  Your Target IP is :' +ip
print '  Scanning :' +ip +'...\n'

for ports in port:
    t = Thread(target=threadScan, args=(site, int(ports)))
    t.start()
