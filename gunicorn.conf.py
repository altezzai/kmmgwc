# gunicorn.conf.py
workers = 3
#bind = "unix:/tmp/gunicorn.sock"
bind = "127.0.0.1:9999"
wsgi_app = "wsgi:application"
chdir = "/home/sn/kmmgwc/kmm"

