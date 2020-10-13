"""
settings

Основной модуль для установления глобальных переменных.

Created at 12.10.2020 by genchik1.
Project IPNinja

"""

__author__ = 'genchik1'
__maintainer__ = 'genchik1'
__status__ = "Development"
__copyright__ = "MIT"

__version__ = "20201012"


import os


IP_LISTS_PATH = os.path.join('data', 'IP_lists.csv')


DB_HOST = 'localhost'
DB_PORT = 27017
DB_NAME = 'ninja-db'

REPO_PATH = os.path.join('git', 'blocklist-ipsets')

IPDATA_API_KEY = 'test'
