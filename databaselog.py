#!/usr/bin/env python
# -*- coding: utf-8 -*-
import psycopg2

# What are the most popular three articles of all time?
query_1_title = ("What are the most popular three articles of all time?")
query_1 = (
    """ select articles.title, count(sliced_path.sliced_name)as num
    from articles, sliced_path where articles.slug = sliced_path.sliced_name
    group by articles.title order by num DESC;
    """)

# Who are the most popular article authors of all time?
query_2_title = ("who are the most popular article authors of all time?")
query_2 = (
    """select authors.name,sum(article_view.views) as views
    from article_view,authors where authors.id = article_view.author
    group by authors.name order by views desc;
    """)

# On which days did more than 1% of requests lead to errors
query_3_title = ("On which days did more than 1% of requests lead to errors?")
query_3 = (
    """select date, numeric from date_percent where numeric >= 1.00;
    """)


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
    print(query_results[1])
    for index, results in enumerate(query_results[0]):
        print(
            index+1, "-", results[0],
            "- ", str(results[1]), "views")


def print_error_results(query_results):
    print(query_results[1])
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
