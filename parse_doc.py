"""
parse_doc

Основной модуль для работы с файдыми .ipset и .netset

Created at 12.10.2020 by genchik1.
Project IPNinja

Примеры использования:

>>> parse_doc('path/file.ipset')
[{'ip':'0.0.0.1', 'list':'level2'}]

"""

__author__ = 'genchik1'
__maintainer__ = 'genchik1'
__status__ = "Development"
__copyright__ = "MIT"

__version__ = "20201012"


import os


def parse_doc(path: str) -> list:
    ips = []

    name = os.path.split(path)[-1].split('.')[0]

    with open(path) as file:
        for f in file:
            if not f.startswith('#'):
                ips.append({'ip': f.replace('\n', ''), 'list': name})

    return ips
