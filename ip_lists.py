"""
ip_lists

Основной модуль для работы со списками IP

Created at 12.10.2020 by genchik1.
Project IPNinja

Примеры использования:

ip_lists(path)

"""

__author__ = 'genchik1'
__maintainer__ = 'genchik1'
__status__ = "Development"
__copyright__ = "MIT"

__version__ = "20201012"


import csv
import json


def ip_lists(path: str) -> tuple:
    lists = []
    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            lists.append(row['List'])

    lists_json = json.dumps(lists)

    return (lists_json, str(len(lists)))
