import psycopg2


class DatabaseQuery():

    DB_NAME = 'news'

    def __init__(self):
        print('Initialising...')
        self.connect()
        print('Ready to go!')

    def connect(self):
        print('Connecting to {}.'.format(self.DB_NAME))
        self.db = psycopg2.connect(dbname=self.DB_NAME)
        self.cursor = self.db.cursor()

    def disconnect(self):
        if not self.db:
            print('Not connected to {}.'.format(self.DB_NAME))
            return
        print('Closing connection to {}.'.format(self.DB_NAME))
        self.db.close()

    def perform_query(self, query, comittal=False):
        print('Executing query {}.'.format(query))
        self.cursor.execute(query)
        if comittal:
            print('Committing changes to the database...')
            self.db.commit()
        print('Query complete.')
        return self.cursor.fetchall()
