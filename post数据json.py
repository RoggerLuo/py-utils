from .config import Config
from urllib import request, parse
import json
def postMessage(data):
    data=json.dumps(data)
    req = request.Request(Config().url) #'http://localhost:9911'
    req.add_header('Content-Type', 'application/json')
    data=data.encode('utf-8')
    with request.urlopen(req,data=data) as f:
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', f.read().decode('utf-8'))

    # print(data)
    # print(data.type)
    # data = parse.urlencode(data)
