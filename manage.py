#!/usr/bin/env python
import os
import sys
#import psycopg2
#import matplotlib.pyplot as plt
#import networkx as nx
#import graph as g


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inv_op.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
    #conn=psycopg2.connect(dbname='tpi', user='nico', host='localhost', password='1234postgre', port=5432)
    #conn.autocommit=True
    #cur=conn.cursor() 
    
