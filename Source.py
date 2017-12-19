#!/usr/bin/env python

# Importing necessary modules for database integration.
import psycopg2


def connect(database_name="news"):
    """Funtion to initiate a database connection"""
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        c = db.cursor()
        return db, c
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


# Class that has the main queries to fetch the Logs Analysis Data
def main():

    db, c = connect()
    # Query 1 to fetch the most popular three articles
    print 'Most popular three articles of all time:'
    c.execute("""SELECT title, count(*) AS views
                 FROM log JOIN articles
                 ON log.path = concat('/article/', articles.slug)
                 GROUP BY title
                 ORDER BY views DESC
                 LIMIT 3;""")
    query1 = c.fetchall()
    for title, views in (query1):
        print '\t', title, '-', views, 'views'
    print ''

    # Query 2 to fetch the most popular article authors
    print 'Most popular article authors of all time-'
    c.execute("""SELECT authors.name AS authorname, count(*) AS views
                 FROM authors, articles, log
                 WHERE authors.id = articles.author
                 AND log.path = concat('/article/', articles.slug)
                 GROUP BY authors.name
                 ORDER BY views DESC;""")
    query2 = c.fetchall()
    for authorname, views in (query2):
        print '\t', authorname, '-', views, 'views'
    print ''

    # Query 3 to fetch the days with more than 1% of requests lead to errors
    print 'Days on which more than 1% of requests lead to errors:'
    c.execute("""SELECT to_char(a.day, 'FMMonth DD, YYYY') AS day,
                 round((100*a.FailReq)/(b.TotalReq)::decimal, 2)
                 AS percentage
                 FROM (SELECT time::date AS day,status,count(*) AS FailReq
                 FROM log
                 WHERE status ='404 NOT FOUND'
                 GROUP BY day,status) a,
                 (SELECT time::date AS day,count(*) AS TotalReq
                 FROM log
                 GROUP BY day) b
                 WHERE a.day = b.day
                 AND round((100*a.FailReq)/(b.TotalReq)::decimal, 2) > 1;""")
    query3 = c.fetchall()
    for day, percentage in (query3):
        print '\t', day, '-', percentage, '%', 'error'
    print ''
    db.close()


if __name__ == "__main__":
    main()
