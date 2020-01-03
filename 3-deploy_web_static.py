#!/usr/bin/python3
"""Creates a .tgz from web_static
and deploys archives to web servers"""
from datetime import datetime
from fabric.operations import local, put, run
from fabric.api import env
from os import path

env.hosts = ['35.243.143.162', '34.74.246.140']


def do_pack():
    """ Tars every file in web_static into versions """
    local("mkdir -p versions")
    path = local("tar -zcvf versions/web_static_{}.tgz web_static".format(
        datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))

    name = "versions/web_static_{}.tgz".format(
        datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"))

    if path.failed:
        return None
    return name


def do_deploy(archive_path):
    """ Deploys archives to web servers """
    if not path.exists(archive_path):
        return False
    try:
        name_put = archive_path[9:]
        name_run = archive_path[9:-4]
        put(archive_path, "/tmp/{}".format(name_put))
        run("mkdir -p /data/web_static/releases/{}/".format(name_run))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(name_put, name_run))
        run("rm /tmp/{}".format(name_put))
        run("mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/releases/{}/".format(name_run, name_run))
        run("rm -fr /data/web_static/releases/{}/web_static"
            .format(name_run))
        run("rm -fr /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(name_run))
        print("New version deployed!")
        return True
    except Exception:
        return False


def deploy():
    """Executes file compression
    and static deployement"""
    pack = do_pack()
    if not pack:
        return False
    return do_deploy(pack)
