#!/usr/bin/env python3
"""
A service exposing metrics from JupyterHub
"""

from functools import wraps
import json
import os
from urllib.parse import quote
import requests

from flask import Flask, redirect, request, Response

from jupyterhub.services.auth import HubAuth


prefix = os.environ.get('JUPYTERHUB_SERVICE_PREFIX', '/')

auth = HubAuth(
    api_token=os.environ['JUPYTERHUB_API_TOKEN'],
    cache_max_age=60,
)

app = Flask(__name__)



@app.route(prefix)
def metrics():
    print(os.environ['JUPYTERHUB_API_TOKEN'])
    r = requests.get("http://localhost:8080/hub/api/users", headers={'Authorization': 'Bearer %s' % os.environ['JUPYTERHUB_API_TOKEN']})
    if r.status_code != 200:
      return Response("Could not load users")
    users = r.json()
    return Response(
        'total_user_count{hostname="%s"} %d' % (os.environ.get("HOSTNAME"), len(users))

        )

def main():
  app.run(port=10101)