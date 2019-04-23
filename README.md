# ws_python

```
$ gunicorn -k flask_sockets.worker app:app

$ gunicorn -c gunicorn.py -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker app:app
```