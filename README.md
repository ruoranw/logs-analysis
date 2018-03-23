# Log Analysis Project

This is a project of Udacity's Full Stack Web Developer Program. The python file responses three questions: 1. What are the most popular three articles of all time? 2. Who are the most popular article authors of all time? 3. On which days did more than 1% of requests lead to errors?

The database's name is *news* and the data is from datanews.sql.

There're three tables in the database. The *authors* table includes information about the authors of articles. The *articles* table includes the articles themselves. The *log* table includes one entry for each time a user has accessed the site.

## Getting Started

In order to get the result, some views have been created.

For the first question, the view that has been created is called `sliced_path` which contains a column of parts of log.path used to compare articles.slug later:

```python
create view sliced_path (sliced_name) as select substring(log.path,10) from log;
```

For the second question, create a view named `article_view` as:

```python
create view article_view as select title,author,count(*) as views
from articles,log where log.path like concat('%',articles.slug)
group by articles.title,articles.author
order by views desc;
```

 Create a view named `date_fail` with date and fail response on that date. Create a view named `date_total_response` with date and total response on that day. Create view named `date_fail_rate` with date and fail responses on that day. Create another view called `date_percent` with column date and numeric. The numeric column is about fail_rate multiply 100.0 then rounded:

```python
 create view date_fail as select time::date as date, count(status) as fails
 from log where status != '200 OK' group by time::date;
```

```python
create view date_total_response as select time::date as date, count (status) as total_response from log group by time::date;
```

```python
create view date_fail_rate as select date_total_response.date as date,
date_fail.fails/date_total_response.total_response::float as fail_rate
from date_total_response, date_fail
where date_total_response.date=date_fail.date
order by fail_rate DESC;
```

```python
create view date_percent as select date,
cast(fail_rate*100.0 as decimal(10,2))
from date_fail_rate;
```


### Prerequisites

You need **vagrant** and **virtual machine** and **postgreSQL** installed.

Clone this repository.

Download the *newsdata.sql* file, and drag it to the folder you just cloned.

### Installing

Open the terminal, the cd to the newsdata.sql file.

For example,

```
cd ...
```

then

```
vagrant up
```

```
vagrant ssh
```
**remember to `cd vagrant`**
```
python databaselog.py
```

## Built With

* vagrant
* virtual machine

## Authors

* **Ruoran Wang**

If you have any questions, contact me at ruoran0502@gmail.com

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
