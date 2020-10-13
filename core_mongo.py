"""
core_mngo

Основной модуль для работы с базой данных MongoDB
Все функции по работе с этой БД, классы и декораторы описаны
только в этом модуле.

Created at 12.10.2020 by genchik1.
Project IPNinja

"""

__author__ = 'genchik1'
__maintainer__ = 'genchik1'
__status__ = "Development"
__copyright__ = "MIT"

__version__ = "20201012"


import os

import settings as s
from parse_doc import parse_doc

from pymongo import MongoClient, ASCENDING


class MongoCore:
    def __init__(self):
        client = MongoClient(s.DB_HOST, s.DB_PORT)
        db = client[s.DB_NAME]
        self.collection = db[s.DB_NAME]
        self.document = {
            'ip': None,
            'list': None
        }

    def _create_index(self):
        self.collection.create_index(
            [
                ("ip", ASCENDING),
                ("list", ASCENDING)
            ],
            name="search"
        )

    def added_new(self):
        self._create_index()

        paths = [os.path.join(s.REPO_PATH, f) for f in os.listdir(s.REPO_PATH)
                 if f.endswith('ipset') or f.endswith('netset')]

        for path in paths:
            data = parse_doc(path)
            for df in data:
                self.collection.insert_one(df)
