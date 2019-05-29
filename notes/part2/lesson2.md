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

## Fact and Dimension Tables

- Work together to create an organized data model
- While fact and dimension are not created differently in the DDL, they are conceptual an extremely important for organization

## Fact Tables

Fact table consists of the measurements, metrics or facts (events that actually happened) of a business process.

Example: customer transactions

## Dimension

A structure that categorizes facts and measures in order to enable users to answer business questions. Dimensions are people, products, place and time.

Example: product information

## Star Schema

Star Schema is the simplest style of data mart schema. The star schema consists of one of more fact tables referencing any number of dimension tables.

## Why "star" schema

- Gets its name from the physical model resembling a star shape
- A fact table is at its center
- Dimension table surrounds the fact table representing the star's points

![star_schema.png](../images/star_schema.png)

## Benefits and Drawbacks of Star Schemas

### Benefits

- denormalized
- simplifies queries
- fast aggregations

### Drawbacks

- issues that come with denormalization
- data integrity
- decrease query flexibility
- many to many relationship

## Snowflake Schema

Logical arrangement of tables in multidimensional database represented by centralized fact tables which are connected to multiple dimensions

![snowflake_schema.png](../images/snowflake_schema.png)

## Snowflake vs Star

- Star schema is a special, simplified case of the snowflake schema
- Star schema does not allow for one to many relationships while the snowflake schema does
- Snowflake schema is more normalized than Star schema but only in 1NF or 2NF, not 3NF

## Data Definition and Constraints

- NOT NULL: the column can't contain a null value
- UNIQUE: all the rows in one column are unique within the table
- PRIMARY KEY: The values in this column identify the rows in the table. If a group of columns are defined as a primary key, they are called a composite key. By default, the primary key constraint has the unique and not null constraint built into it.

## Upsert

IN RDBMS language, teh term _upset_ refers to the idea of inserting a new row in an existing table, or updating the row if it already exists in the table. The action of updating or inserting has been described as "upsert".

## ON CONFLICT

Let's say we want to insert the following data.

```SQL
INSERT into customer_address
VALUES (432, '758 Main Street', 'Chicago', 'IL');
```

but we are not sure whether or not this data conflicts the existing records. In this case, we can use **ON CONFLICT DO NOTHING / DO UPDATE**.

```SQL
ON CONFLICT (customer_id)
DO NOTHING;
```

```SQL
ON CONFLICT (customer_id)
DO UPDATE
    SET customer_street  = EXCLUDED.customer_street;
```

## Wrap Up

We learned:

- What is a relational database
- OLAP vs OLTP
- Normalization
- Denormalization
- Fact vs Dimension Tables
- Star and Snowflake schemas
