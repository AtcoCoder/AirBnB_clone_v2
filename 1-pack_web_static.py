#!/usr/bin/python3
"""Script that distributes an archive to web servers using
 the function do_pack"""
from fabric.api import *
from datetime import datetime
import os


def do_pack():
    """Generates archive of all file in web_static folder"""
    path = "versions/"
    if not os.path.exists(path):
        os.mkdir(path)
    created_at = datetime.now().strftime('%Y%m%d%H%M%S')
    local('tar -czvf {}web_static_{}.tgz web_static'.format(path, created_at))
