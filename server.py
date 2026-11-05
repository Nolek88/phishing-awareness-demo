#!/usr/bin/env python3
"""
Server locale per la demo.
- Serve index.html
- Riceve i POST su /notify e li stampa in modo leggibile + salva su log.txt
"""
import json
import os
import socket
import textwrap
from datetime import datetime
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

PORT = 8000
LOG_FILE = "log.txt"
LINE = "═" * 65
SUB  = "─" * 65


def ip_locale():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"


def format_block(ts, evento, data, wrap_width=95):
    lines = [LINE]
    lines.append(f"  🕐  {ts}")
    lines.append(f"  🎯  {evento}")
    if data:
        lines.append(SUB)
        label_width = min(max((len(k) for k in data), default=10), 24)
        for k, v in data.items():
            value = str(v)
            avail = max(wrap_width - label_width - 5, 20)
            wrapped = textwrap.wrap(value, avail) or [""]
            lines.append(f"  {k.ljust(label_width)} : {wrapped[0]}")
            for extra in wrapped[1:]:
                lines.append(f"  {' ' * label_width}   {extra}")
    lines.append(LINE)
    return "\n".join(lines)


class Handler(SimpleHTTPRequestHandler):
    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def do_POST(self):
        if self.path != "/notify":
            self.send_response(404)
            self.end_headers()
            return

        length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(length).decode("utf-8", errors="replace")
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            data = {"evento": "raw", "message": raw}

        evento = data.pop("evento", "evento")
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        block = format_block(ts, evento, data)

        print("\n" + block, flush=True)
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(block + "\n\n")

        self.send_response(200)
        self._cors()
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"ok":true}')

    def do_OPTIONS(self):
        self.send_response(200)
        self._cors()
        self.end_headers()

    def log_message(self, fmt, *args):
        pass


if __name__ == "__main__":
    ip = ip_locale()
    print(LINE)
    print(f"  🚀 Server attivo")
    print(f"  Sul tuo PC:    http://localhost:{PORT}/demo-login.html")
    print(f"  Da tuo padre:  http://{ip}:{PORT}/demo-login.html   (stessa Wi-Fi)")
    print(f"  Log su:        {os.path.abspath(LOG_FILE)}")
    print(f"  Ctrl+C per fermare")
    print(LINE)
    ThreadingHTTPServer(("0.0.0.0", PORT), Handler).serve_forever()