bind = "unix:/run/gunicorn.sock"
command = "/app2/env/bin/gunicorn"
pythonpath = "/app2/appdev"
workers = 3
accesslog = "/app2/logs/gunicorn.access.log"
errorlog = "/app2/logs/gunicorn.app.log"
capture_output = True
loglevel = "info"
