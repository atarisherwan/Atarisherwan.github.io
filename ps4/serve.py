#!/usr/bin/env python3
"""Serve locally for a PS4; proper MIME types for modules, binary and AppCache."""
import os
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

class Handler(SimpleHTTPRequestHandler):
    extensions_map = dict(SimpleHTTPRequestHandler.extensions_map,
        **{'.js':'text/javascript', '.mjs':'text/javascript',
           '.bin':'application/octet-stream', '.appcache':'text/cache-manifest',
           '.manifest':'text/cache-manifest'})
    def end_headers(self):
        if self.path.split('?')[0].lower().endswith(('.html','.js','.mjs','.bin','.manifest','.appcache')):
            self.send_header('Cache-Control','no-cache, must-revalidate')
        super().end_headers()

if __name__ == '__main__':
    port=int(sys.argv[1]) if len(sys.argv)>1 else 8081
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print('ATARI SHERWAN HOST listening on port %d'%port, flush=True)
    print('PHONE: http://127.0.0.1:%d/   PS4: http://PHONE_WIFI_IP:%d/'%(port,port),flush=True)
    ThreadingHTTPServer(('0.0.0.0',port),Handler).serve_forever()
