#!/usr/bin/env python3

import http.client
import json
from urllib.parse import quote
import sys

def send_request(ip, port, content):
    connection = http.client.HTTPConnection(ip, port)
    query = json.dumps(content)
    encoded_query = quote(query)
    connection.request("GET", "/?data=" + encoded_query)
    
    response = connection.getresponse()
    data = response.read().decode()
    print(data)
    
    connection.close()

def get_content(x):
    if not x.startswith('{'):
        try:
            with open(x, 'r') as f:
                content = json.load(f)
        except FileNotFoundError:
            print('File not found.')
            raise
        except json.JSONDecodeError:
            print('Invalid JSON file.')
            raise
    else:
        content = json.loads(x)
    
    return content


if __name__ == '__main__':
    args = sys.argv

    if len(args) < 2:
        print('No argument. Run --help for help.')
        sys.exit(1)

    if len(args) > 2:
        print('Too many arguments. Run --help for help.')
        sys.exit(1)

    if args[1] == '--help':
        print('Usage: client.idea.py <IP> <PORT> <JSON-like data>')
        sys.exit(0)
    
    ip = 'localhost'
    port = 8000

    arg = args[1]

    try:
        content = get_content(arg)
    except Exception as e:
        sys.exit(1)

    send_request(ip, port, content)