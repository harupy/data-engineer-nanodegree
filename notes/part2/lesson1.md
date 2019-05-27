# Part 2 - Lesson 1: Introduction to Data Modeling

## What is a Data Model?

An abstraction that organizes elements of data and how they will relate to each other

## Why is Data Modeling Important?

You don't want to do a join on four tables to just get a customer email, right?

## Who does Data Modeling?

- data scientist
- soft engineers
- anyone involved in the process of using and analyzing data

So really **EVERYONE**!

## Relation Databases

Rows and columns (= Table)

- Oracle
- Teradata
- MySQL
- PostgreSQL
- Splite

## When to use a relational database

- Ese of use -- SQL
- Ability to JOINs
- Ability to aggregations and analytics
- Smaller data volumes
- Easier to change business requirements
- Flexibility of queries
- Modeling that data not modeling queries
- Secondary indexes available
- ACID transactions --data integrity

## ACID Transactions

- **A**tomicity: the whole transaction is processed or nothing is processed (all or nothing)
- **C**onsistency: only transactions that abide by constraints and rules is written into the database otherwise database keeps previous state
- **I**solation: transactions are processed independently and securely, order does not matter
- **D**urability: completed transactions are saved to database even of cases of system failure

## When NOT to use a relational database

- have large amounts of data
- need to be able to store different data type formats
- need hight throughput -- fast reads
- need a flexible schema
- need high availability
- need horizontal scalability

## What is PostgreSQL

- Open source object-relational database system
- Uses and build on SQL language

## NoSQL Database

- has been around also since the 1970s
- became mush more popular and use during the 2000s as data sizes increased
- has a simpler design, simpler horizontal scaling, and finer control of availability
- NoSQL = Not Only SQL; NoSQL and NonRelational are interchangeable terms
- various types of NoSQL databases

## Common types of NoSQL databases

- Apache Cassandra (Partition Row store)
- MongoDB (Document store)
- DynamoDB (Key-Value store)
- Apache HBase (Wide Column store)
- Neo4J (Graph database)

## Basics of Cassandra

![basics_of_cassandra](../images/basics_of_cassandra.png)

## What is Apache Cassandra?

> provides **scalability** and **high availability** without compromising performance. Linear scalability nad proven **fault-tolerane** on commodity hardware or cloud infractructure make it the perfect platform for mission-critical data.
> -- Apache Cassandra Documentation

- Apache Cassandra uses its own query language CQL (Cassandra Query Language)

## When to use a NoSQL DB

- large amounts of data (NoSQL database is built for big data)
- need horizontal scalability
- need high throughput -- fast reads
- need a flexible schema
- need high availability
- need to be able to store different data type formats
- users are distributed -- low latency

These are the reasons to not use a RDB!

## When NOT to use a NoSQL DB?

- need ACID Transactions
- need ability to do JOINs
- ability to do aggregations and analytics
- have changing business requirements
- queries are not available and need to have flexibility
- have a small dataset

These are the reasons to use a RDB!

## REMEMBER

NoSQL DB and RDB **DON'T replace** each other for all tasks. Both do different tasks extremely well, and should be utilized for the use cases they fit best.

## Wrap Up

We learned

- what is data modeling?
- who does data modeling?
- when to and not to use RDB
- when to and not to use NoSQL RDB
- how to create a simple table in PostgreSQL
- how to create a simple table in Apache Cassandra
