from pyquent.natural_deduction import dict_to_latex
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from pyquent.utils import LATEX_FONT_SIZE
from pyquent import Pyquent
import argparse
import json

pyquent = Pyquent()

def parse_to_latex(s):
    if not s:
        return s

    parse_tree = pyquent.parse(s)
    output = pyquent.transform(parse_tree)
    return output.to_latex()

def math(s, size=10):
    if isinstance(s, dict):
        s = dict_to_latex(s, parser=parse_to_latex)
    return LATEX_FONT_SIZE[size-1]+s

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        parsed_path = urlparse(self.path)
        query = parse_qs(parsed_path.query)
        
        tree = query['data']
        tree = tree[0]
        tree = json.loads(tree)

        self.wfile.write(('$$\n'+str(math(tree))+'\n$$').encode())

def parse_args():
    parser = argparse.ArgumentParser(description="Send a JSON-like data request to a specified IP and port.")
    parser.add_argument("--ip", type=str, default="localhost", help="IP address of the server (default: localhost)")
    parser.add_argument("--port", type=int, default=8000, help="Port of the server (default: 8000)")
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    server = HTTPServer(('localhost', args.port), SimpleHTTPRequestHandler)
    #print(f"Listening on port {args.port}")
    server.serve_forever()