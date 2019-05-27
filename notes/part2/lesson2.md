# Part 2 - Lesson 2: Relational Data Models

## Objective

Learn the fundamentals of how to do relational data modeling by focusing on normalization, denormalization, fact/dimension tables, and different schema models.

## Database

Definition: A set of related data and the way it is organized.

## Database Management System

consisting of **computer software** that allows users to interact with the databases and provide access to all of the data. Because of the **close relationship** the term database is often used to refer to both the database and the DBMS used.

## Importance of Relational Databases

- Invented in 1969 by researchers at IBM. Edgar R. Codd, the lead researcher, proposed 12 rules of what makes a database management system a true relational system.

Ruel1: The information rule:
All information in a RDB is represented explicitly at the logical level and in exactly one way - by values in tables.

## Relational Importance

- standardization of data model
- flexibility in adding and altering tables
- data integrity
- stand query language
- simplicity
- intuitive organization (e.g. spreadsheet format)

## OLAP vs OLTP

**Online Analytical Processing (OLAP)**:<br>
Databases optimized for these workloads allow for complex analytical and ad hoc queries. These type of databases are optimized for reads.

**Online Transactional Processing (OLTP)**:<br>
Databases optimized for these workloads allow for less complex queries in large volume. The types of queries for these databases are read, insert, update, and delete.

## Structuring Your Database

- Normalization: To reduce data redundancy (copies of data) and increase data integrity (means that the answer I get back from the database is the correct answer)
- Denormalization: Must be done in read heavy workloads to increase performance.

Unnormalized table:
![unnormalized_table.png](../images/unnormalized_table.png)

## Objectives of Normal Form

1. To free the database from unwanted insertions, updates, and deletion dependencies
2. To reduce the need for refactoring the database as new types of data are introduced
3. To make the relational model more informative to users
4. To make the database neutral to the query statistics

## Normal Forms

- First Normal Form (1NF)
- Second Normal Form (2NF)
- Third Normal Form (3NF)

1NF:
![1nf.png](../images/1nf.png)

2NF:
![2nf.png](../images/2nf.png)

3NF:
![3nf.png](../images/3nf.png)
