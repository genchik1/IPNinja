"""
main

Основной модуль для работы api

Created at 12.10.2020 by genchik1.
Project IPNinja

"""

__author__ = 'genchik1'
__maintainer__ = 'genchik1'
__status__ = "Development"
__copyright__ = "MIT"

__version__ = "20201012"


import os
import sqlite3
import argparse

from flask import Flask

from ip_lists import ip_lists
from ip_network import ip_with_netmask
from repo_sync import RepoSync
from core_mongo import MongoCore
from firehole_api import ipdatas
import settings as s


app = Flask(__name__)
app.config.from_object(__name__)

iplist, niplist = ip_lists(s.IP_LISTS_PATH)


def init():
    if not os.path.exists(RepoSync().repo_path):
        print('git clone...')
        RepoSync().clone_repo()
        print('create db and added data...')
        MongoCore().added_new()
    else:
        d = RepoSync().diff()


@app.route("/api/iplist")
def get_iplist():
    return iplist


@app.route("/api/niplist")
def get_niplist():
    return niplist


@app.route("/api/ip_with_netmask/<path:ip>")
def get_ip_with_netmask(ip):
    out = ip_with_netmask(ip)
    out = str(out)
    return out


@app.route("/api/ipdata/<path:ip>")
def get_ipdata(ip):
    out = ipdatas(ip)
    return out


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(title='subcommands',
                                   description='valid subcommands',
                                   help='description')

init_parser = subparsers.add_parser('init', help='Команда для запуска \
    загрузки репозитория https://github.com/firehol/blocklist-ipsets \
    и загрузки данных из списков в mongodb.')
init_parser.set_defaults(func=init)

iplist_parser = subparsers.add_parser('iplist', help='Получить \
    все имена списков.')
iplist_parser.set_defaults(func=get_iplist)

niplist_parser = subparsers.add_parser('niplist', help='Получить \
    кол-во уникальных списков.')
niplist_parser.set_defaults(func=get_niplist)

ip_with_netmask_parser = subparsers.add_parser('ip_with_netmask',
                                               help='Функция вхождения ip в подсеть.')
ip_with_netmask_parser.add_argument('-ip', dest='ip', help='IP адрес \
    и маска подсети в формате 69.78.70.144/29 или 69.78.70.144/255.255.255.254')
ip_with_netmask_parser.set_defaults(func=get_ip_with_netmask)

ipdata_parser = subparsers.add_parser('ipdata', help='Функция \
    для получения данных по IP адресу, реализована на api https://ipdata.co/')
ipdata_parser.add_argument('-ip', dest='ip', help='IP адрес')
ipdata_parser.set_defaults(func=get_ipdata)


if __name__ == '__main__':

    # app.run(debug=True)

    args = parser.parse_args()
    try:
        print(args.func(args.ip))
    except TypeError:
        print(args.func())
