#!/usr/bin/env python

from distutils.core import setup

setup(name='jupyterhub_metrics_service',
      version='0.1',
      description='JupyterHub Prometheus Metrics exporter service',
      author='Vašek Pavlín',
      author_email='vasek@redhat.com',
      entry_points={
        'console_scripts': [
            'jupyterhub_metrics_service=jupyterhub_metrics_service:main',
        ],
      },
      py_modules=['jupyterhub_metrics_service'],
      install_requires=['Flask']
     )