# 🎓 Inventory Management & Business Reporting System

A Python and PostgreSQL based inventory management application designed
to help small and medium-sized businesses manage products, suppliers,
categories, purchases, sales, stock levels, and business reports.

The project demonstrates practical implementation of **Python,
PostgreSQL, SQL, CRUD operations, relational joins, database
normalization, transactions, exception handling, and business
reporting**.

------------------------------------------------------------------------

## 📌 Project Overview

The Inventory Management System provides a simple command-line interface
for managing inventory records and generating useful business reports.

The application connects Python to PostgreSQL using `psycopg2` and
performs database operations through SQL queries.

### Main objectives

-   Manage product records
-   Manage product categories and suppliers
-   Track inventory stock
-   Record purchases
-   Record sales
-   Automatically update stock quantities
-   Search products
-   Generate inventory reports
-   Generate sales and revenue reports
-   Generate category-wise reports
-   Demonstrate transaction management with commit and rollback

------------------------------------------------------------------------

## 🚀 Features

### 1. Product Management

-   Add new products
-   View all products
-   View product details
-   Update product information
-   Delete products
-   Search products by name

### 2. Inventory Management

-   Track current stock
-   Set reorder levels
-   Identify products requiring reorder
-   Calculate total inventory value

### 3. Purchase Management

When stock is purchased:

1.  A purchase record is inserted into the `purchases` table.
2.  Product stock is increased.
3.  Both operations are committed as one transaction.

### 4. Sales Management

When a product is sold:

1.  Product stock is checked.
2.  The sale is recorded.
3.  Product stock is reduced.
4.  The transaction is committed only if all operations succeed.
5.  If stock is insufficient, the transaction is rolled back.

### 5. Business Reports

The system provides:

-   Inventory Report
-   Sales Report
-   Category Report
-   Inventory Dashboard
-   Total inventory value
-   Total sales revenue
-   Product-wise sales quantity

------------------------------------------------------------------------

## 🛠️ Technologies Used

  Technology   Purpose
  ------------ ---------------------------------
  Python       Application development
  PostgreSQL   Relational database
  SQL          Database operations and reports
  psycopg2     Python-PostgreSQL connectivity
  OOP          Application structure
  Git          Version control
  GitHub       Project hosting

------------------------------------------------------------------------

## 🗄️ Database Design

The database is normalized into multiple related tables.

``` text
                    categories
                         |
                         |
                         v
                     products
                    /         \
                   /           \
                  v             v
             purchases        sales

                     products
                         |
              ---------------------
              |
              v
          suppliers
```

### Tables

#### `categories`

Stores product categories.

``` text
category_id
category_name
```

#### `suppliers`

Stores supplier information.

``` text
supplier_id
supplier_name
email
phone
city
```

#### `products`

Stores product and inventory information.

``` text
product_id
product_name
category_id
supplier_id
price
stock_quantity
reorder_level
```

#### `purchases`

Stores incoming inventory transactions.

``` text
purchase_id
product_id
quantity
purchase_price
purchase_date
```

#### `sales`

Stores outgoing inventory transactions.

``` text
sale_id
product_id
quantity
sale_price
sale_date
```

------------------------------------------------------------------------

## 📁 Project Structure

``` text
inventory_management/
│
├── database/
│   └── schema.sql
│
├── config.py
├── db.py
├── models.py
├── inventory_manager.py
├── reports.py
├── main.py
├── requirements.txt
└── README.md
```

### File Description

  -----------------------------------------------------------------------
  File                                Description
  ----------------------------------- -----------------------------------
  `database/schema.sql`               Creates database tables,
                                      constraints, indexes, and sample
                                      data

  `config.py`                         PostgreSQL connection configuration

  `db.py`                             Creates PostgreSQL database
                                      connections

  `models.py`                         Contains application model classes

  `inventory_manager.py`              Implements CRUD, search, purchase,
                                      and sales operations

  `reports.py`                        Implements dashboards and business
                                      reports

  `main.py`                           Provides the command-line
                                      application menu

  `requirements.txt`                  Contains Python dependencies
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# ⚙️ Installation and Setup

## 1. Clone the Repository

``` bash
git clone https://github.com/YOUR_USERNAME/inventory_management.git
```

Move into the project:

``` bash
cd inventory_management
```

------------------------------------------------------------------------

## 2. Create a Virtual Environment

Windows:

``` bash
python -m venv venv
```

Activate it:

``` bash
venv\Scripts\activate
```

If PowerShell blocks activation, you can also run the project using the
Python executable inside the environment.

------------------------------------------------------------------------

## 3. Install Dependencies

``` bash
pip install -r requirements.txt
```

The project uses:

``` text
psycopg2-binary
```

------------------------------------------------------------------------

# 🐘 PostgreSQL Setup

## 1. Create the Database

Open PostgreSQL/pgAdmin and create:

``` sql
CREATE DATABASE inventory_db;
```

------------------------------------------------------------------------

## 2. Run the Database Schema

Open:

``` text
database/schema.sql
```

Execute the complete SQL script against the `inventory_db` database.

The script creates:

-   Categories
-   Suppliers
-   Products
-   Purchases
-   Sales
-   Indexes
-   Sample data

------------------------------------------------------------------------

## 3. Configure Database Credentials

Open:

``` text
config.py
```

Update the PostgreSQL password:

``` python
DB_CONFIG = {
    "host": "localhost",
    "database": "inventory_db",
    "user": "postgres",
    "password": "YOUR_POSTGRES_PASSWORD",
    "port": 5432
}
```

Replace:

``` text
YOUR_POSTGRES_PASSWORD
```

with your local PostgreSQL password.

### Security Note

Do not commit real database passwords to GitHub.

For a production version, use environment variables such as `.env`.

------------------------------------------------------------------------

# ▶️ Run the Application

From the project root:

``` bash
python main.py
```

The application displays:

``` text
==================================================
     INVENTORY MANAGEMENT SYSTEM
==================================================
1. Dashboard
2. View Products
3. Add Product
4. Update Product
5. Delete Product
6. Search Product
7. Purchase Stock
8. Sell Product
9. Inventory Report
10. Sales Report
11. Category Report
0. Exit
==================================================
Enter your choice:
```

------------------------------------------------------------------------

# 📊 Application Workflow

``` text
                    USER
                      |
                      v
                  main.py
                      |
                      v
             InventoryManager
                      |
          +-----------+-----------+
          |                       |
          v                       v
       CRUD                 Transactions
          |                       |
          +-----------+-----------+
                      |
                      v
                    db.py
                      |
                      v
                  psycopg2
                      |
                      v
                PostgreSQL
                      |
       +--------------+--------------+
       |              |              |
       v              v              v
   products       purchases        sales
       |
       +------ categories
       |
       +------ suppliers
```

------------------------------------------------------------------------

# 🔄 CRUD Operations

The project demonstrates all four major CRUD operations.

### Create

``` sql
INSERT INTO products
```

Used when adding products.

### Read

``` sql
SELECT
```

Used for viewing and searching products.

### Update

``` sql
UPDATE products
```

Used for modifying product details and stock.

### Delete

``` sql
DELETE FROM products
```

Used for removing products.

------------------------------------------------------------------------

# 🔗 SQL JOINs

The application combines normalized data using relational joins.

Example:

``` sql
SELECT
    p.product_name,
    c.category_name,
    s.supplier_name,
    p.price,
    p.stock_quantity
FROM products p
JOIN categories c
    ON p.category_id = c.category_id
JOIN suppliers s
    ON p.supplier_id = s.supplier_id;
```

This avoids storing repeated category and supplier information inside
every product record.

------------------------------------------------------------------------

# 💳 Transaction Management

Transactions are used for purchase and sales operations.

### Purchase transaction

``` text
INSERT purchase
       ↓
UPDATE stock
       ↓
COMMIT
```

### Sale transaction

``` text
Check stock
       ↓
INSERT sale
       ↓
UPDATE stock
       ↓
COMMIT
```

If an operation fails:

``` text
ERROR
  ↓
ROLLBACK
```

For example, attempting to sell more products than are available
produces an error and prevents the database from being left in an
inconsistent state.

------------------------------------------------------------------------

# 📈 Reports

## Inventory Report

Displays:

-   Product
-   Category
-   Supplier
-   Price
-   Current stock
-   Reorder level
-   Stock status

Example:

``` text
Product       : Laptop
Category      : Electronics
Supplier      : Tech World Supplies
Price         : ₹55000
Stock         : 15
Reorder Level : 5
Status        : OK
```

------------------------------------------------------------------------

## Sales Report

Calculates:

``` text
Product
Quantity Sold
Revenue
```

Revenue is calculated using:

``` text
Quantity × Sale Price
```

------------------------------------------------------------------------

## Category Report

Displays:

``` text
Category
Number of Products
Total Stock
Inventory Value
```

------------------------------------------------------------------------

## Dashboard

The dashboard summarizes:

``` text
Total Products
Total Stock
Inventory Value
Total Sales Revenue
```

------------------------------------------------------------------------

## 🧪 Testing the Application

Recommended testing sequence:

``` text
1. Dashboard
2. View Products
3. Add Product
4. View Products
5. Update Product
6. Search Product
7. Purchase Stock
8. Sell Product
9. Sales Report
10. Inventory Report
11. Category Report
12. Dashboard
```

### Transaction Test

Try selling more units than the available stock.

Example:

``` text
Product ID: 1
Quantity: 1000
```

The system should reject the sale and roll back the transaction.

------------------------------------------------------------------------

## 🔐 Database Constraints

The database uses:

-   Primary Keys
-   Foreign Keys
-   `NOT NULL`
-   `UNIQUE`
-   `CHECK`
-   Indexes

Example:

``` sql
stock_quantity INT NOT NULL DEFAULT 0
CHECK (stock_quantity >= 0)
```

This prevents negative inventory values at the database level.

------------------------------------------------------------------------

## 📌 Key SQL Concepts Demonstrated

This project provides practical experience with:

``` text
SELECT
INSERT
UPDATE
DELETE
WHERE
LIKE
JOIN
LEFT JOIN
GROUP BY
ORDER BY
SUM()
COUNT()
COALESCE()
CASE
PRIMARY KEY
FOREIGN KEY
UNIQUE
CHECK
INDEX
TRANSACTION
COMMIT
ROLLBACK
```

------------------------------------------------------------------------

## 🎯 Learning Outcomes

After completing this project, you should be able to explain:

-   How Python connects to PostgreSQL
-   How a normalized relational database is designed
-   How primary and foreign keys work
-   How SQL joins combine related tables
-   How CRUD operations are implemented
-   How transactions protect data consistency
-   How commit and rollback work
-   How SQL aggregation is used for business reports
-   How Python handles database exceptions
-   How to structure a Python database application

------------------------------------------------------------------------
## 🖥️ Project Outcome
### pgsql:
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/ea544cd5-0e1b-4d94-9d31-3d65e138dc57" />
### python main file output:
<img width="685" height="885" alt="image" src="https://github.com/user-attachments/assets/b70121a8-4d1c-41aa-959e-dd5dddda46ef" />
<img width="838" height="846" alt="image" src="https://github.com/user-attachments/assets/af2e1f20-4d4c-43dd-a5f3-e43a183f953c" />
<img width="789" height="832" alt="image" src="https://github.com/user-attachments/assets/d31c3230-cec2-457f-99fc-c2c3c7a7984e" />
<img width="724" height="836" alt="image" src="https://github.com/user-attachments/assets/7269d237-7654-4c0d-8c7b-2c0d36f50350" />
<img width="848" height="812" alt="image" src="https://github.com/user-attachments/assets/fcb4628f-2382-48a6-949a-6b68460abf27" />
<img width="769" height="841" alt="image" src="https://github.com/user-attachments/assets/092c3e99-c1bb-4d4e-a134-901cbd855334" />
<img width="730" height="830" alt="image" src="https://github.com/user-attachments/assets/b7c996d7-974f-4e7c-b98e-e895817119e1" />
<img width="815" height="570" alt="image" src="https://github.com/user-attachments/assets/7f3f86d3-c469-41c8-892d-35fd6945eb30" />

------------------------------------------------------------------------

## 🔮 Future Enhancements

Possible improvements include:

-   Tkinter graphical user interface
-   Login and role-based access
-   Admin and Manager roles
-   Product image uploads
-   CSV/Excel report export
-   PDF report generation
-   Low-stock notifications
-   Supplier management UI
-   Date-range sales reports
-   Charts and dashboards
-   REST API using FastAPI
-   React frontend
-   Docker deployment
-   Environment variable configuration
-   Unit and integration testing

------------------------------------------------------------------------

## 👨‍💻 Author

**Bachina Sai Harshith**

GitHub: `https://github.com/saiharshith123/inventory_management`

------------------------------------------------------------------------

## 📄 License

This project is licensed under open source.

------------------------------------------------------------------------

## ⭐ Project Highlights

``` text
Python
      +
PostgreSQL
      +
SQL
      +
Database Normalization
      +
CRUD
      +
JOINs
      +
Transactions
      +
Business Reports
```
