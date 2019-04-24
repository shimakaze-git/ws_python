pkill -f 'gunicorn'
# gunicorn -c gunicorn.py -k "geventwebsocket.gunicorn.workers.GeventWebSocketWorker" app:app
gunicorn -b 0.0.0.0:8080 -k "geventwebsocket.gunicorn.workers.GeventWebSocketWorker" app:app