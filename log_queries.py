from database_query import DatabaseQuery


def most_popular_articles(dbq):
    q = (
        "select articles.title, reqs.num from (select log.path, count(*) as num from log where log.path like '/article/%' and log.method = 'GET' group by log.path) as reqs, articles where reqs.path like concat('/article/', articles.slug) order by reqs.num desc limit 3;"
    )
    result = dbq.perform_query(q)
    print(result)


def most_popular_authors(dbq):
    pass


def http_error_days(dbq):
    pass


if __name__ == '__main__':
    dbq = DatabaseQuery()
    print('Question 1:')
    most_popular_articles(dbq)
    print('Question 2:')
    most_popular_authors(dbq)
    print('Question 3:')
    http_error_days(dbq)
    dbq.disconnect()
