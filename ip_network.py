"""
ip_network

Основной модуль для работы с IP и маской подсети

Created at 12.10.2020 by genchik1.
Project IPNinja

Примеры использования:

>>> ip_with_netmask('5.79.79.210/31')
True
>>> ip_with_netmask('5.79.79.210/29')
False

"""

__author__ = 'genchik1'
__maintainer__ = 'genchik1'
__status__ = "Development"
__copyright__ = "MIT"

__version__ = "20201012"


import ipaddress


def ip_with_netmask(ip: str) -> bool:
    try:
        ipaddress.ip_network(ip)
        return True
    except:
        return False
