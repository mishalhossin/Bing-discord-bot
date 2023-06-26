import threading
from flask import Flask
import os
import sys
import logging

app = Flask("keepalive")

@app.route('/', methods=['GET', 'POST', 'CONNECT', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'TRACE', 'HEAD'])
def main():
    return '''Hey there, User! To keep your Replit running continuously, you'll need to use an uptime monitoring service like UptimeRobot'''

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
app.logger.disabled = True
cli = sys.modules['flask.cli']
cli.show_server_banner = lambda *x: None

def run_flask_app():
    app.run(host='0.0.0.0', port=3000, debug=False, use_reloader=False)


def run_flask_in_thread():
    threading.Thread(target=run_flask_app).start()

if __name__ == "__main__":
    run_flask_in_thread()
