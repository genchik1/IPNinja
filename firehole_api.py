"""
ip_network

Основной модуль для работы с AIP https://ipdata.co/

Created at 12.10.2020 by genchik1.
Project IPNinja

Примеры использования:
 
>>> get_ipdata('69.78.70.144')
{'asn': {'asn': 'AS6167',
         'domain': 'verizonwireless.com',
         'name': 'Cellco Partnership DBA Verizon Wireless', 
         'type': 'business'},
 'calling_code': '1',
 'carrier': {'mcc': '310', 'mnc': '004', 'name': 'Verizon'},
 'city': None,
 'continent_code': 'NA',
 'continent_name': 'North America',
 'count': '2',
 'country_code': 'US',
 'country_name': 'United States',
 'currency': {'code': 'USD',
              'name': 'US Dollar',
              'native': '$',
              'plural': 'US dollars',
              'symbol': '$'},
 'emoji_flag': '🇺🇸',
 'emoji_unicode': 'U+1F1FA U+1F1F8',
 'flag': 'https://ipdata.co/flags/us.png',
 'ip': '69.78.70.144',
 'is_eu': False,
 'languages': [{'name': 'English', 'native': 'English'}],
 'latitude': 37.751,
 'longitude': -97.822,
 'postal': None,
 'region': None,
 'region_code': None,
 'status': 200,
 'threat': {'is_anonymous': False,
            'is_bogon': False,
            'is_known_abuser': False,
            'is_known_attacker': False,
            'is_proxy': False,
            'is_threat': False,
            'is_tor': False},
 'time_zone': {'abbr': 'CDT',
               'current_time': '2020-10-12T20:21:15.793388-05:00',
               'is_dst': True,
               'name': 'America/Chicago',
               'offset': '-0500'}}

"""

__author__ = 'genchik1'
__maintainer__ = 'genchik1'
__status__ = "Development"
__copyright__ = "MIT"

__version__ = "20201012"

import json
from ipdata import ipdata

import settings as s


def ipdatas(ip):
    ip_data = ipdata.IPData(s.IPDATA_API_KEY)
    response = ip_data.lookup(ip)
    return response
