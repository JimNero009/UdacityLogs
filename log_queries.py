#!/usr/bin/env python3

from database_query import DatabaseQuery


def most_popular_articles(dbq):
    q = """
        select articles.title, reqs.num from
        (select log.path, count(*) as num
        from log where log.path like '/article/%'
        and log.method = 'GET' group by log.path) as reqs, articles
        where reqs.path like concat('/article/', articles.slug)
        order by reqs.num desc limit 3;
    """
    result = dbq.perform_query(q)
    for row in result:
        print('{} - {} views'.format(row[0], row[1]))
    print('******************')


def most_popular_authors(dbq):
    q = """
       select authors.name, views.sum from
       (select articles.author, sum(reqs.num) as sum from
       (select log.path, count(*) as num from log
       where log.path like '/article/%'
       and log.method = 'GET' group by log.path)
       as reqs, articles where
       reqs.path like concat('/article/', articles.slug)
       group by articles.author) as views, authors
       where authors.id = views.author order by sum desc;
    """
    result = dbq.perform_query(q)
    for row in result:
        print('{} - {} views'.format(row[0], row[1]))
    print('******************')


def http_error_days(dbq):
    q = """
        select total_reqs.date,
        cast(bad_reqs.total_bad as decimal)/cast(total_reqs.total as decimal)
        as error_rate from (select date(time) as date,
        count(log.status) as total from log group by date(log.time)
        order by date(log.time)) as total_reqs,
        (select date(time) as date, count(log.status)
        as total_bad from log where log.status != '200 OK'
        group by date(log.time) order by date(log.time)) as bad_reqs
        where total_reqs.date = bad_reqs.date and
        cast(bad_reqs.total_bad as decimal)
        /cast(total_reqs.total as decimal) > 0.01
    """
    result = dbq.perform_query(q)
    for row in result:
        print('{} - {}%% errors'.format(row[0], int(row[1] * 10000)/100.))
    print('******************')


if __name__ == '__main__':
    dbq = DatabaseQuery()
    print('The most popular three articles of all time:')
    most_popular_articles(dbq)
    print('The most popular article authors of all time:')
    most_popular_authors(dbq)
    print('Days where more than 1%% of requests led to errors:')
    http_error_days(dbq)
    dbq.disconnect()
