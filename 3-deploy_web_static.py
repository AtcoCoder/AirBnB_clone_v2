#!/usr/bin/python3
"""Script that distributes an archive to web servers using
 the function do_pack"""
from fabric.api import *
from datetime import datetime
import os
do_deploy = __import__('2-do_deploy_web_static').do_deploy
do_pack = __import__('1-pack_web_static').do_pack


env.hosts = ['35.153.19.110', '100.25.46.48']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def deploy():
    archive_path = do_pack()
    if not os.path.exists(archive_path):
        return False
    return do_deploy(archive_path)
