# ws_python

```
$ gunicorn -k flask_sockets.worker -b 0.0.0.0:8080 app:app

$ gunicorn -c gunicorn.py -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -b 0.0.0.0:8080 app:app
```