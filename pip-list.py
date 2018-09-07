import json
import subprocess
import sys
import os

try:
    distobjs = subprocess.check_output([sys.executable, '-m', 'pip', 'list', '--disable-pip-version-check', '--format=json'])
    distobjs = distobjs.decode("utf-8")
    distobjs = json.loads(distobjs)
    dists = {}
    for obj in distobjs:
        dval = {}
        dval['value'] = obj['version']
        dists[obj['name']] = dval
    output_template = '{ "name": "com.myorganization.pipinventory", "protocol_version": "2", "integration_version": "0.1.0", "data": [ { "entity": { "name": "instance-1", "type": "custom" }, "inventory": {} } ] }'
    output_map = json.loads(output_template)
    output_map['data'][0]['inventory'] = dists
    print(json.dumps(output_map))
except SystemExit as e:
    pass
