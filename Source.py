#!/usr/bin/env python3

# Importing necessary modules for database integration.
import psycopg2


def connect(database_name="news"):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        c = db.cursor()
        return db, c
    except:
        print("Unable to connect to the database")


# Class that has the main queries to fetch the Logs Analysis Data
def main():

    db, c = connect()
    # Query 1 to fetch the most popular three articles
    print 'Most popular three articles of all time:'
    c.execute("select title, count(*) as views from log join articles on "
        "log.path = concat('/article/', articles.slug) group by title "
        "order by views desc limit 3;")  # noqa
    query1 = c.fetchall()
    for i in range(len(query1)):
        print '\t', query1[i][0], '-', query1[i][1], 'views'
    print ''

    # Query 2 to fetch the most popular article authors
    print 'Most popular article authors of all time-'
    c.execute("select authors.name, count(*) as views from authors, articles,"
        " log where authors.id = articles.author and log.path = "
        "concat('/article/', articles.slug) group by authors.name "
        "order by views desc;")  # noqa
    query2 = c.fetchall()
    for i in range(len(query2)):
        print '\t', query2[i][0], '-', query2[i][1], 'views'
    print ''

    # Query 3 to fetch the days with more than 1% of requests lead to errors
    print 'Days on which more than 1% of requests lead to errors:'
    c.execute("select a.day, ((100*a.FailReq)/(b.TotalReq)::float) from "
        "(select to_char(time,'YYYY-MM-DD') as day,status,count(*) as FailReq"
        " from log where status ='404 NOT FOUND' group by day,status) a, "
        "(select to_char(time,'YYYY-MM-DD') as day,count(*) as TotalReq "
        "from log group by day) b where to_date(a.day,'YYYY-MM-DD') = "
        "to_date(b.day,'YYYY-MM-DD') and "
        "((100*a.FailReq)/(b.TotalReq)::float) > 1")  # noqa
    query3 = c.fetchall()
    for i in range(len(query3)):
        print '\t', query3[i][0], '-', query3[i][1], '%', 'error'
    print ''
    db.close()


if __name__ == "__main__":
    main()
