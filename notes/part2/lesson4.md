# Part 2 - Lesson 4: NoSQL Data Models

## Learning Objective

Learn the fundamentals of data modeling for NoSQL databases

## Apache Cassandra

- **Open Source** NoSQL DB
- Masterless Architecture
- High Availability
- Linearly Scalable
- Used by Uber, Netflix, Hulu, Twitter, Facebook, etc
- Major contributors to the project: DataStax, Facebook, Twitter, Apple

## Distributed Databases

In a distributed database, in order to have high availability, you will need copies of your data.

## Eventual Consistency:

Over time (if no new changes are made) each copy of the data will be the same, but if there are new changes, the data may be different in different locations. The data may be inconsistent for only milliseconds. There are workarounds in place to prevent getting stale data (The workarounds are outside the scope of this course).

## The CAP Theorem

A theorem in computer science that states it is **impossible** for a distributed data store to **simultaneously provide** more than two out of the following guarantees of consistency, availability, and partition tolerance.

- Consistency: Every read from the database gets the latest (and correct) piece of data or an error
- Availability: Every request is received and a response is given -- without a guarantee that the data is the latest update
- Partition Tolerance: The system continues to work regardless of losing network connectivity between nodes

Apache Cassandra is an AP (Availability and Partition tolerant) database.

## Denormalization in Apache Cassandra

Denormalization in Apache Cassandra is **absolutely** critical. Think about your **queries** first. There are no `JOINS` in Apache Cassandra.

## Data Modeling in Apache Cassandra

- Denormalization is a must
- Denormalization must be done for fast reads
- Apache Cassandra has been optimized for fast writes
- **ALWAYS** think queries first
- One table per query is a great strategy
- Apacke Cassandra does **NOT** allow for JOINs between tables

## CQL

- Stands for **C**assandra **Q**uery **L**anguage
- Similar to SQL
- No `JOINS`, `GROUP BY` or subqueries

## Primary Key

- Must be unique
- The PRIMARY KEY is made up of either just the PARTITION KEY or may also include additional CLUSTERING COLUMNS
- A simple PRIMARY KEY is just one column that is also the PARTITION KEY. A composite PRIMARY KEY is made up more that one column and will assist in creating a unique value and in your retrieval queries
- The PARTITION KEY will determine the distribution of data across the system

## Clustering Columns

- The clustering column will sort the data in sorted **ascending** order, e.g., alphabetical order.
- More than one clustering column can be added (or none!)
- From there the clustering columns will sort in order of how they were added to the primary key

## WHERE Clause

- Data Modeling in Apache Cassandra is query focused, and that focus needs to be on the **WHERE** clause.
- The **PARTITION KEY** must be included in your query and any **CLUSTERING COLUMNS** can be used in the order they appear in your **PRIMARY KEY**
- The **WHERE** clause must be included to execute queries. It is recommended that one partition be queried at a time for performance implications. It is possible to do a `select * from table` if you add a configuration **ALLOW FILTERING** to your query. This is risky, but available if absolutely necessary.

[database - Difference between partition key, composite key and clustering key in Cassandra? - Stack Overflow](https://stackoverflow.com/questions/24949676/difference-between-partition-key-composite-key-and-clustering-key-in-cassandra)

> In a situation of **COMPOSITE** primary key, the "first part" of the key is called **PARTITION KEY** (in this example **key_part_one** is the partition key) and the second part of the key is the **CLUSTERING KEY** (in this example **key_part_two**)

## Lesson Wrap Up

- Basics of Distributed Database Design
- Must know your queries and model the tables to your queries
- Importance of Denormalization
- Apache Cassandra is a popular NoSQL database
- CQL and some key differences with SQL
- Primary Key, Partition Key, and Clustering Column
- The WHERE clause

## Course Wrap Up

- Relational vs Non-Relational Databases
- Fundamentals Relational Database Data Modeling
- Normalization
- Denormalization]
- Basics of Distributed Database Design
- Basics of Distributed Database Design
-
