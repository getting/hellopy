import threading
import time
from urllib.request import urlopen

n = 0
lock = threading.Lock()

hosts = ["http://yahoo.com", "http://google.com", "http://amazon.com", "http://ibm.com", "http://apple.com"]

t = time.time()

for host in hosts:
    res = urlopen(host)
    print(res.read(1024))

print(time.time() - t)