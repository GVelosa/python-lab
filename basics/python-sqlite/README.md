# SQLite Basics (Safe Queries)

> 📺 This project was largely developed by following the video below, although some parts of the code were implemented and adapted by me:
> 👉 https://youtu.be/YPD0YEjqe90?si=O6A1R23n9AzatgI8

---

This script is part of my personal Python laboratory and focuses on studying **database operations using SQLite with safe query practices**.

It covers the fundamental concepts of CRUD:

- Create → Insert new records into the database
- Read → Retrieve data using queries
- Update → Modify existing records
- Delete → Remove records (included as a commented example)

The goal is to understand how to interact with a database using Python while following **good security practices**, especially using **parameterized queries** to avoid SQL injection.

---

## Overview

The script creates and manipulates a simple database called `banco.db`, simulating a basic banking system.

It demonstrates how to:

* Create a database and table
* Insert data with random values (safely)
* Query records
* Update existing data
* Display results

---

## Technologies Used

* Python
* SQLite (`sqlite3`)
* Random data generation (`random`)

---

## Structure

* [Database Creation](#database-creation)
* [Safe Data Insertion](#safe-data-insertion)
* [Data Query](#data-query)
* [Data Update](#data-update)
* [Visualization](#visualization)

---

## Database Creation

The script creates a table called `contas_bancarias` if it does not already exist.

### Table structure:

* `id`: Unique identifier (auto-increment)
* `titular`: Account holder name
* `saldo`: Account balance
* `cpf`: Unique identifier for each user (must be unique)

### Concepts covered:

* SQL table creation
* Primary key
* Constraints (`NOT NULL`, `UNIQUE`)

---

## Safe Data Insertion

A new record is inserted using **parameterized queries**:

```python
cursor.execute("""
INSERT INTO contas_bancarias (titular, saldo, cpf)
VALUES (?, ?, ?)
""", ('Cassio', rand_saldo, rand_cpf))
```

### Concepts covered:

* Parameterized queries (`?`)
* Safe data handling
* Separation between SQL and data

### Why this matters:

* Prevents **SQL Injection**
* Ensures safer handling of user input
* Follows real-world backend best practices

---

## Data Query

The script retrieves all accounts:

```python
cursor.execute("SELECT id, titular, saldo FROM contas_bancarias")
contas = cursor.fetchall()
```

### Concepts covered:

* SQL `SELECT`
* Fetching multiple records with `fetchall()`

---

## Data Update

The script updates the balance of a specific account (`id = 15`):

```python
cursor.execute("""
UPDATE contas_bancarias
SET saldo = 9000
WHERE id = 15
""")
```

### Concepts covered:

* SQL `UPDATE`
* Conditional updates with `WHERE`

---

## Visualization

The results are printed in the console.

### Features:

* Filters a specific account (`id = 15`)
* Displays updated data
* Uses formatted output (`f-strings`)

### Concepts covered:

* Looping through query results
* Tuple unpacking
* Conditional filtering in Python

---

## Notes

* This script is intended for **learning purposes only**
* Parameterized queries are used for **secure data insertion**
* The `DELETE` operation is included but commented out for safety
* The update is hardcoded (`id = 15`) for demonstration purposes

---

## Purpose

This project is part of my learning journey to:

* Understand how databases work in practice
* Learn secure interaction between Python and SQL
* Build a foundation for backend and data-driven applications

It is not intended for production use, but it follows **practices used in real systems**.
