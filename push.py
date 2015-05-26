#!/usr/bin/env python
import json
import urllib2
import sys


msg = str(sys.argv[1])
json_data = {
    "collapse_key": "msg",
    "data": {
        "message": {
            "id": "89988598032",
            "vehicle": {
                "number": "KA 1234",
                "type": "Sedan"
            },
            "name": "Shyam",
            "mobile": "+91-1234567890"
        }
    },
    "registration_ids": ["APA91bEsbzViOy_udpUoiGg4QqteOTALWOvOT9L9QJoLkTCD2ODvxh9Ymtcmdw0wG5kYnd3V0ZJa-RSoGIsecPBws9whL3wHcM6v5p1abn-vWPn_JH819DIT7UPcog71-VwbwEi-cZ_NwWlk547EJ7TRnQXZedlDqsTUwVtsfJtoXJDxWoc9MTU"],
}

url = 'https://android.googleapis.com/gcm/send'
myKey = "AIzaSyACaleLhwaVxrVRZ-yFvKneW-Ufmmk-IM4"
data = json.dumps(json_data)

headers = {'Content-Type': 'application/json',
           'Authorization': 'key=%s' % myKey}

req = urllib2.Request(url, data, headers)
f = urllib2.urlopen(req)
response = json.loads(f.read())

print json.dumps(response, sort_keys=True, indent=2)
