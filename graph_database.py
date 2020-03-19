from py2neo import Graph

GRAPH_DB_CONN = Graph("bolt://127.0.0.1:7687", user="mayajun", password="123456", secure=True)