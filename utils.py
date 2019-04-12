"""Reusable functionality"""

import os
import psycopg2
from stuff.environment_variables import DB_HOST, DB_NAME, DB_USER, DB_PWD


def get_pg_connection_attr():
    """ Get Postgres connection """

    return "host={0} dbname={1} user={2} password={3}".format(
        os.environ.get('DB_HOST', DB_HOST),
        os.environ.get('DB_NAME', DB_NAME),
        os.environ.get('DB_USER', DB_USER),
        os.environ.get('DB_PWD', DB_PWD))


def log_call(uuid, layer, timestamp, time_interval, result):
    pg_connection = psycopg2.connect(get_pg_connection_attr())
    pg_cursor = pg_connection.cursor()
    pg_cursor.execute(
        "insert into \"Resilience\".\"LOG_TEST\" values ('{0}', '{1}', '{2}', '{3}', '{4}'); COMMIT;"
             .format(uuid, layer, timestamp, time_interval, result))
    pg_cursor.close()
    pg_connection.close()
