# -*- coding: utf-8 -*-
import json
import subprocess
import sys

from threading import Thread
from urllib.request import urlopen
from http.server import HTTPServer, BaseHTTPRequestHandler, urllib

from stereo import *
from navigate import *

class CVRequestHandler(BaseHTTPRequestHandler):
    stereo = Stereo()

    def get_state(self):
        return self.stereo.get_state()

    def get_decription(self):
        return self.stereo.description

    def get_object_list(self):
        return self.stereo.object_list

    def get_picture(self, camera = 'left'):
        return self.stereo.saveimage(img = self.stereo.snapshot(camera))

    def do_recognize(self, data):
        print(data, file = sys.stderr)
        return self.stereo.recognize('left')

    def do_find(self, data):
        print(data, file = sys.stderr)
        return dict(a=0)

    def do_scan(self, data):
        print(data, file = sys.stderr)
        A_min = max(-140, int(data['a_min'][0]))
        A_max = min( 140, int(data['a_max'][0]))
        _ = self.stereo.scan(A_min, A_max)
        json.dump(_, open('/tmp/log', 'w'), indent = 2)
        return _

    def do_rotate(self, data):
        print(data, file = sys.stderr)
        return self.stereo.rotate(data, returnimage = int(data['returnimage'][0]))

    def do_range(self, data):
        print(data, file = sys.stderr)
        return dict(a=0)

    def do_cloud(self, data):
        print(data, file = sys.stderr)
        return dict(a=0)


    def load_file(self, name, context=None, content_type='text/html'):
        self.send_response(200)
        self.send_header('Content-type', content_type)
        self.end_headers()
        data = ''
        with open(name, 'rb') as _file:
            data = _file.read()
        if context:
            for key in context:
                data = data.replace(
                    bytes(key, 'utf-8'),
                    bytes(context[key], 'utf-8')
                )
        self.wfile.write(data)

    def load_str(self, data):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes(data, 'utf-8'))
    #
    def from_camera(self, url):
        #'http://192.168.0.122:5555/describe'
        response = urlopen(url)
        return json.loads(response.read().decode("utf-8"))

    def to_json(self, data):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(str.encode(json.dumps(data)))

    def do_GET(self):
        print(self.path, file = sys.stderr)
        if self.path.endswith('png'):
            self.load_file(self.path.lstrip('/'), content_type='image/png')
        elif self.path.endswith('jpg'):
            self.load_file(self.path.lstrip('/'), content_type='image/jpeg')
        elif self.path.startswith('/static'):
            content_type = 'text/html'
            if self.path.endswith('jpg'):
                content_type = 'image/jpeg'
            elif self.path.endswith('css'):
                content_type = 'text/css'
            self.load_file(self.path.lstrip('/'), content_type=content_type)
        elif self.path.startswith('/state'):
            self.to_json(self.get_state())
        elif self.path.startswith('/describe'):
            self.to_json(self.get_decription())
        elif self.path.startswith('/list_objects'):
            self.to_json(self.get_object_list())
        elif self.path.startswith('/left'):
            self.to_json(self.get_picture(camera = 'left'))
        elif self.path.startswith('/right'):
            self.to_json(self.get_picture(camera = 'right'))
        elif self.path.startswith('/wide'):
            self.to_json(self.get_picture(camera = 'wide'))
        elif self.path == "/exit":
            self.load_str('')
            global need_to_exit
            need_to_exit = True
            self.server.server_close()
            exit(0)
        else:
            self.load_file('index.html')

    def do_POST(self):
        print(self.path, file = sys.stderr)
        data = urllib.parse.parse_qs(
           self.rfile.read(
               int(self.headers.get('content-length'))
           ).decode('utf-8')
        )
        if self.path.startswith('/recognize'):
            self.to_json(self.do_recognize(data))
        elif self.path.startswith('/find'):
            self.to_json(self.do_find(data))
        elif self.path.startswith('/scan'):
            self.to_json(self.do_scan(data))
        elif self.path.startswith('/rotate'):
            self.to_json(self.do_rotate(data))
        elif self.path.startswith('/range'):
            self.to_json(self.do_range(data))
        elif self.path.startswith('/cloud'):
            self.to_json(self.do_cloud(data))
        else:
            self.load_str('wrong path')

    def log_message(self, format, *args):
        return


if __name__ == "__main__":
    server = HTTPServer(('0.0.0.0', 8000), CVRequestHandler)
    try:
        server.serve_forever()
    except:
        need_to_exit = True

