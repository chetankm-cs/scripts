import urllib2
import os
import time

ports = ["8081", "8091", "25001"]
status = {}
t = 10
for port in ports:
    status[port] = False

while True:
    for port in ports:
        try:
            urllib2.urlopen("http://localhost:"+port+"/healthcheck").read()
            if not status[port]:
                status[port] = True
                os.system("terminal-notifier -message '"+repr(int(port)-1)+"' -open 'http://localhost:"+repr(int(port)-1)+"'")
        except urllib2.HTTPError as e:
            status[port] = False
            pass
        except urllib2.URLError as e:
            status[port] = False
            pass

    time.sleep(t)