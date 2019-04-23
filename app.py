# -*- coding: utf-8 -*-

import json
import datetime
import time

from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler

from flask import Flask, request, render_template

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/pipe')
def pipe():
    if request.environ.get('wsgi.websocket'):
        ws = request.environ['wsgi.websocket']

        while True:
            time.sleep(1)
            message = ws.receive()

            if message is None:
                break

            datetime_now = datetime.datetime.now()
            data = {
                'time': str(datetime_now),
                'message': message
            }
            ws.send(json.dumps(data))

            print(message)
            print(data)

    return


if __name__ == '__main__':
    app.debug = True

    host = 'localhost'
    port = 8080
    host_port = (host, port)

    server = WSGIServer(
        host_port,
        app,
        handler_class=WebSocketHandler
    )
    server.serve_forever()
