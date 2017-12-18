#!/usr/bin/env python3


import psycopg2


dname = "news"

try:
    db = psycopg2.connect('dbname=news')
    c = db.cursor()
except:
    print "Unable to connect to the database"


def main():

    print 'Most popular three articles of all time:'
    c.execute("select b.title,a.artcount from (select path,count(*) as artcount from log group by path order by artcount desc,path) as a, articles b where a.path like '%'||b.slug||'%' limit 3;")  # noqa
    query1 = c.fetchall()
    for i in range(len(query1)):
        print '\t', query1[i][0], '-', query1[i][1], 'views'
    print ''

    print 'Most popular article authors of all time:'
    c.execute("select A.name as AuthorName,sum(B.Views) as ViewCount FROM AUTHORS A, (select b.title as ArticleTitle,b.slug as SlugID, b.author as AuthorID,a.artcount as Views from (select path,count(*) as artcount from log group by path order by artcount desc, path) as a, articles b where a.path like '%'||b.slug||'%') as B where A.id=B.AuthorID group by A.name order by ViewCount desc;")  # noqa
    query2 = c.fetchall()
    for i in range(len(query2)):
        print '\t', query2[i][0], '-', query2[i][1], 'views'
    print ''

    print 'Days on which more than 1% of requests lead to errors:'
    c.execute("select Day, Percentage from (select a.day, (cast((100*a.FailReq) as integer)/cast(b.TotalReq as integer)::float) as Percentage from (select to_char(time,'YYYY-MM-DD') as day,status,COUNT(*) as FailReq from log where status ='404 NOT FOUND' group by day,status) a, (select to_char(time,'YYYY-MM-DD') as day,COUNT(*) as TotalReq from log group by day) b  where to_date(a.day,'YYYY-MM-DD') = to_date(b.day,'YYYY-MM-DD')) as Percent where Percentage > 1.0")  # noqa
    query3 = c.fetchall()
    for i in range(len(query3)):
        print '\t', query3[i][0], '-', query3[i][1], '%', 'error'
    print ''
    db.close()


if __name__ == "__main__":
    main()