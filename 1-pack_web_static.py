#!/usr/bin/python3
"""Creates a .tgz from web_static"""
from datetime import datetime
from fabric.operations import local


def do_pack():
    """ Tars every file in web_static into versions """
    local("mkdir -p versions")
    path = local("tar -zcvf versions/web_static_{}.tgz web_static".format(
        datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))

    if path.failed:
        return None
    return path
