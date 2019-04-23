pkill -f 'gunicorn'
gunicorn -c gunicorn.py -k "geventwebsocket.gunicorn.workers.GeventWebSocketWorker" app:app
