# Log Analysis Project

This is a project of Udacity's Full Stack Web Developer Program. The python file responses three questions: 1. What are the most popular three articles of all time? 2. Who are the most popular article authors of all time? 3. On which days did more than 1% of requests lead to errors?

The database is datanews.sql and I used postgresql to build it.

There're three tables. The authors table includes information about the authors of articles. The articles table includes the articles themselves. The log table includes one entry for each time a user has accessed the site.

## Getting Started

In order to get the result, some views have been created.

For the first question, the view that has been created is called sliced_path which contins a column of parts of log.path used to compare articles.slug later.

For the second question, join articles and authors tables to create a view named authors_articles with author and their articles. Create a view named date_fail with date and fail response on that date.Create a view named date_total_response with date and total response on that day. Create view named date_fail_rate with date and fail responses on that day. Create another view called date_percent with column date and numeric. The numeric column is about fail_rate multiply 100.0 then rounded.

### Prerequisites

You need vagrant and virtual machine installed. Download the newsdata.sql file, and drag it to the folder which also contains the vagrant configuration file. You should also have postgreSQL installed to run it.

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
```
python db-log.py
```

## Built With

* vagrant
* virtual machine

## Authors

* **Ruoran Wang**

If you have any questions, contact me at ruoran0502@gmail.com

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
