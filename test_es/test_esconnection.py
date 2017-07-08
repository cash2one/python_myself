# -*- coding: utf-8 -*-
import random
import requests
from elasticsearch import Transport
from elasticsearch.connection import RequestsHttpConnection
from config.base_config import ES_HOSTS, ES_INDEX, ES_CONNECTION_NUM

hosts = []
for host in ES_HOSTS:
    hosts.append({'url': host})

connection_pool = Transport(hosts, connection_class=RequestsHttpConnection).connection_pool

def get_es_conn():
    return connection_pool.get_connection()

def search(query):
    con = get_es_conn()
    status, headers, data = con.perform_request('GET', '/'+ES_INDEX+'/_search?q='+query)
    return data
# -----------------------------------------------------
import json
from es_client import search

query_str = "((title:*"+keyword+"*)OR(key_words:*"+keyword+"*))AND(is_public:true)AND(publish_time:[0 TO "+str(int(time.time()))+"])"
query_str += "&size=" + str(page_size)
query_str += "&from=" + str((page - 1) * page_size)
res = json.loads(search(query_str))