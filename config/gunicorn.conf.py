bind = "0.0.0.0:80"
workers = 3
accesslog = "/app2/logs/gunicorn.access.log"
errorlog = "/app2/logs/gunicorn.app.log"
capture_output = True
loglevel = "info"