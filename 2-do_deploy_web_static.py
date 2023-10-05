#!/usr/bin/python3
"""Script that distributes an archive to web servers using
 the function do_pack"""
from fabric.api import *
from datetime import datetime
import os

env.hosts = ['35.153.19.110', '100.25.46.48']

def do_deploy(archive_path):
    """Generates archive of all file in web_static folder"""
    if not os.path.exists(archive_path):
        return False
    put(archive_path, '/tmp/')
    archive_file = run('ls /tmp/ | grep web_static_')
    if archive_file.failed:
        return False
    extracted_files = archive_file.split('.')[0]
    release_path = '/data/web_static/releases/{}'.format(extracted_files)
    result = sudo('tar -xvf {} /tmp/{}'.format(release_path, archive_file))
    if result.failed:
        return False
    result = sudo('rm /tmp/{}'.format(archive_file))
    if result.failed:
        return False
    result = sudo('unlink /data/web_static/current')
    if result.failed:
        return False
    result = sudo('ln -s {} /data/web_static/current'.format(release_path))
    if result.failed:
        return False
    return True
