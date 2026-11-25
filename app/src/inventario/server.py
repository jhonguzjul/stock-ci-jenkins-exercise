"""Servidor HTTP mínimo (solo librería estándar) con un endpoint /health."""

import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

from . import __version__


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            cuerpo = json.dumps({"estado": "ok", "version": __version__}).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(cuerpo)))
            self.end_headers()
            self.wfile.write(cuerpo)
        else:
            self.send_error(404, "No encontrado")


def run():
    puerto = int(os.environ.get("PORT", "8000"))
    print(f"Inventario {__version__} escuchando en el puerto {puerto}", flush=True)
    HTTPServer(("0.0.0.0", puerto), Handler).serve_forever()
