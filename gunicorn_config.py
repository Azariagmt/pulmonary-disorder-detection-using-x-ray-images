import os
port = int(os.environ.get("PORT", 33507))
bind = f"0.0.0.0:{port}"
workers = 1
threads = 1
timeout = 1000000