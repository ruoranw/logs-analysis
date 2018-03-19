#!/usr/bin/env python
# -*- coding: utf-8 -*-
import psycopg2

# What are the most popular three articles of all time?
query_1_title = ("What are the most popular three articles of all time?")
query_1 = (
"""create view sliced_path (sliced_name) as select substring(log.path,10) from log;
"""

""" select articles.title, count(sliced_path.sliced_name)as num
from articles, sliced_path where articles.slug = sliced_path.sliced_name
group by articles.title order by num DESC;
""")

# Who are the most popular article authors of all time?
query_2_title = ("who are the most popular article authors of all time?")
query_2 = (
"""create view popular_articles as select articles.title as articles_name,
count(sliced_path.sliced_name)as num from articles, sliced_path
where articles.slug = sliced_path.sliced_name
group by articles.title order by num DESC;
"""
"""create view authors_articles as
select articles.title as article, authors.name as author from articles, authors
where articles.author = authors.id;
"""
"""select authors_articles.author, count (popular_articles.num) as total_views
from authors_articles, popular_articles
where authors_articles.article = popular_articles.articles_name
group by authors_articles.author order by total_views DESC;
"""
)

# On which days did more than 1% of requests lead to errors
query_3_title = ("On which days did more than 1% of requests lead to errors?")
query_3 = (
"""create view date_fail as select time::date as date, count(status) as fails
from log where status != '200 OK' group by time::date;
"""
"""create view date_fail_rate as select date_total_response.date as date,
date_fail.fails/date_total_response.total_response::float as fail_rate
from date_total_response, date_fail
where date_total_response.date=date_fail.date order by fail_rate DESC;
"""
"""create view date_percent as select date, cast(fail_rate*100.0 as decimal(10,2))
from date_fail_rate;
"""
"""select date, numeric from date_percent where numeric >= 1.00;
"""
)

def connect(database_name="news"):
    """ Connect to the database. Return to a database connection."""
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("Unable to connect to database.")

def get_query_results(query):
    """ Return query results for given query"""
    db, cursor = connect()
    cursor.execute(query)
    return cursor.fetchall()
    db.close()

def print_query_results(query_results):
    print (query_results[1])
    for index, results in enumerate(query_results[0]):
        print(
            index+1, "-", results[0],
            "- ", str(results[1]), "views")

def print_error_results(query_results):
    print (query_results[1])
    for results in query_results[0]:
        print(results[0], "-", str(results[1]) + " % errors")

if __name__ == '__main__':
    # store query results
    popular_articles_results = get_query_results(query_1), query_1_title
    popular_authors_results = get_query_results(query_2), query_2_title
    load_error_days = get_query_results(query_3), query_3_title

    # print query results
    print_query_results(popular_articles_results)
    print_query_results(popular_authors_results)
    print_error_results(load_error_days)
