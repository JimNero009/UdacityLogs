#!/usr/bin/env python3

import psycopg2


class DatabaseQuery():

    DB_NAME = 'news'

    def __init__(self):
        self.connect()

    def connect(self):
        self.db = psycopg2.connect(dbname=self.DB_NAME)
        self.cursor = self.db.cursor()

    def disconnect(self):
        if not self.db:
            return
        self.db.close()

    def perform_query(self, query, comittal=False):
        self.cursor.execute(query)
        if comittal:
            self.db.commit()
        return self.cursor.fetchall()
