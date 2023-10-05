#!/usr/bin/python3
"""Script that distributes an archive to web servers using
 the function do_play"""
from fabric.api import *
from datetime import datetime


def do_deploy():
    """Generates archive of all file in web_static folder"""

    created_at = datetime.now().strftime('%Y%m%d%H%M%S')
    local('tar -czvf web_static_{}'.format(created_at))
