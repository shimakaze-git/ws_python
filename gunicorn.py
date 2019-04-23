# -*- coding: utf-8 -*-
import multiprocessing

name = 'websocket_chat'

# Process Naming
proc_name = 'gunicorn'

# Logging
logfile = './logs/{}.log'.format(name)
loglevel = 'info'
logconfig = None

# Server Socket
bind = '0.0.0.0:8000'
# bind = '127.0.0.1:8080'

# Worker Processes
worker_class = 'gevent'
workers = multiprocessing.cpu_count() * 2 + 1
# workers = 5
worker_connections = 1024
# max_requests = 1000
max_requests = 5120
timeout = 120
keepalive = 2

backlog = 2048


# Server Mechanics
preload_app = True
debug = True
reload = debug
daemon = True
pidfile = 'gunicorn.pid'

# daemon = False

# secure_scheme_headers = {
#     'X-FORWARDED-PROTOCOL': 'ssl',
#     'X-FORWARDED-PROTO':    'https',
#     'X-FORWARDED-SSL':      'on',
# }
