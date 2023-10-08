#!/usr/bin/python3
"""Script that distributes an archive to web servers using
 the function do_pack"""
from fabric.api import *
from datetime import datetime
import os


env.hosts = ['35.153.19.110', '100.25.46.48']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'

def do_deploy(archive_path):
    """Generates archive of all file in web_static folder"""
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        archive_file = run('ls /tmp/ | grep web_static_')
        extracted_files = archive_file.split('.')[0]
        release_path = '/data/web_static/releases/{}/'.format(extracted_files)
	sudo('mkdir -p {}'.format(release_path))
        sudo('tar -xzf /tmp/{} -C {}'.format(archive_file, release_path))
        sudo('rm /tmp/{}'.format(archive_file))
	sudo('mv {}/web_static/* {}'.format(release_path, release_path))
	sudo('rm -rf {}/web_static'.format(release_path))
        sudo('rm -rf /data/web_static/current')
        sudo('ln -s {} /data/web_static/current'.format(release_path))
    except Exception:
        return False
    return True
