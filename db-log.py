import psycopg2
# Connect to an existing database
conn = psycopg2.connect("dbname=news")
# Open a cursor to perform database operations
cur = conn.cursor()
# Create a to view contains parts of log.path used to compaire articles.slug
# later query the database
# cur.execute("create view sliced_path (sliced_name) as select substring(log.path,10) from log;")
# conn.commit()

# The query for the first question
cur.execute("select articles.title, count(sliced_path.sliced_name)as num from articles, sliced_path where articles.slug = sliced_path.sliced_name group by articles.title order by num DESC;")
results = cur.fetchall()
print results
conn.close()

# Create a view of question one that have articles title and each one's view count
# conn = psycopg2.connect("dbname=news")
# cur = conn.cursor()
# cur.execute("create view popular_articles as select articles.title as articles_name, count(sliced_path.sliced_name)as num from articles, sliced_path where articles.slug = sliced_path.sliced_name group by articles.title order by num DESC;")
# conn.commit()
# conn.close()

# join articles and authors tables to create a view named authors_articles with author and their articles. This view is for Q2 later use.
# conn = psycopg2.connect("dbname=news")
# cur = conn.cursor()
# cur.execute("create view authors_articles as select articles.title as article, authors.name as author from articles, authors where articles.author = authors.id;")

# Create a view with date and fail response on that date for Q3 use
# cur.execute("create view date_fail as select time::date as date, count(status) as fails from log where status != '200 OK' group by time::date;")

# Create a view with date and total response on that day for Q3 use
# cur.execute("create view date_total_response as select time::date as date, count (status) as total_response from log group by time::date;")

# Create view with date and fail responses on that day for Q3 use.
# cur.execute("create view date_fail_rate as select date_total_response.date as date, date_fail.fails/date_total_response.total_response::float as fail_rate from date_total_response, date_fail where date_total_response.date=date_fail.date order by fail_rate DESC;")

# Create another view called date_percent with column date and numeric(fail_rate*100.0 then rounded)
# cur.execute("create view date_percent as select date, cast(fail_rate*100.0 as decimal(10,2))from date_fail_rate;")

# conn.commit()
# conn.close()

# This is the query of Q2
conn = psycopg2.connect("dbname=news")
cur = conn.cursor()
cur.execute("select authors_articles.author, count (popular_articles.num) as total_views from authors_articles, popular_articles where authors_articles.article = popular_articles.articles_name group by authors_articles.author order by total_views DESC;")
results = cur.fetchall()
print results
conn.close()

# This is the query of Q3
conn = psycopg2.connect("dbname=news")
cur = conn.cursor()
cur.execute("select date, numeric from date_percent where numeric >= 1.00;")
results = cur.fetchall()
print results
conn.close()