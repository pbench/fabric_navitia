# coding=utf-8

# Copyright (c) 2001-2015, Canal TP and/or its affiliates. All rights reserved.
#
# This file is part of fabric_navitia, the provisioning and deployment tool
#     of Navitia, the software to build cool stuff with public transport.
#
# Hope you'll enjoy and contribute to this project,
#     powered by Canal TP (www.canaltp.fr).
# Help us simplify mobility and open public transport:
#     a non ending quest to the responsive locomotion way of traveling!
#
# LICENCE: This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# Stay tuned using
# twitter @navitia
# IRC #navitia on freenode
# https://groups.google.com/d/forum/navitia
# www.navitia.io

from fabric.api import env, task, roles, sudo
from fabfile.utils import _upload_template
from fabtools import require

@task
@roles('haproxy')
def configure():
    _upload_template('haproxy/haproxy.cfg', '/etc/haproxy/haproxy.cfg',
                     context={
                        'env': env,
                     },
                     user='haproxy')

@task
@roles('haproxy')
def setup():
    require.deb.packages(['haproxy'], update=True)


@task
@roles('haproxy')
def restart():
    sudo("systemctl restart haproxy")

@task
@roles('haproxy')
def reload():
    sudo("systemctl reload haproxy")

@task
@roles('haproxy')
def start():
    sudo("systemctl start haproxy")

@task
@roles('haproxy')
def stop():
    sudo("systemctl stop haproxy")

@task
@roles('haproxy')
def status():
    sudo("systemctl status haproxy")
