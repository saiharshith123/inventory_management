DROP TABLE IF EXISTS sales CASCADE;
DROP TABLE IF EXISTS purchases CASCADE;
DROP TABLE IF EXISTS products CASCADE;
DROP TABLE IF EXISTS suppliers CASCADE;
DROP TABLE IF EXISTS categories CASCADE;

CREATE TABLE categories (
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE suppliers (
    supplier_id SERIAL PRIMARY KEY,
    supplier_name VARCHAR(150) NOT NULL,
    email VARCHAR(150) UNIQUE,
    phone VARCHAR(20),
    city VARCHAR(100)
);

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(150) NOT NULL,
    category_id INT NOT NULL,
    supplier_id INT NOT NULL,
    price NUMERIC(10,2) NOT NULL CHECK (price >= 0),
    stock_quantity INT NOT NULL DEFAULT 0
        CHECK (stock_quantity >= 0),
    reorder_level INT NOT NULL DEFAULT 10
        CHECK (reorder_level >= 0),

    CONSTRAINT fk_product_category
        FOREIGN KEY (category_id)
        REFERENCES categories(category_id),

    CONSTRAINT fk_product_supplier
        FOREIGN KEY (supplier_id)
        REFERENCES suppliers(supplier_id)
);

CREATE TABLE purchases (
    purchase_id SERIAL PRIMARY KEY,
    product_id INT NOT NULL,
    quantity INT NOT NULL CHECK (quantity > 0),
    purchase_price NUMERIC(10,2) NOT NULL
        CHECK (purchase_price >= 0),
    purchase_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_purchase_product
        FOREIGN KEY (product_id)
        REFERENCES products(product_id)
);


CREATE TABLE sales (
    sale_id SERIAL PRIMARY KEY,
    product_id INT NOT NULL,
    quantity INT NOT NULL CHECK (quantity > 0),
    sale_price NUMERIC(10,2) NOT NULL
        CHECK (sale_price >= 0),
    sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_sale_product
        FOREIGN KEY (product_id)
        REFERENCES products(product_id)
);

CREATE INDEX idx_products_category
ON products(category_id);

CREATE INDEX idx_products_supplier
ON products(supplier_id);

CREATE INDEX idx_purchases_product
ON purchases(product_id);

CREATE INDEX idx_sales_product
ON sales(product_id);

CREATE INDEX idx_sales_date
ON sales(sale_date);

INSERT INTO categories (category_name)
VALUES
('Electronics'),
('Stationery'),
('Furniture'),
('Accessories');

INSERT INTO suppliers
(supplier_name, email, phone, city)
VALUES
('Tech World Supplies',
 'techworld@gmail.com',
 '9876543210',
 'Hyderabad'),
('Office Mart',
 'officemart@gmail.com',
 '9876543211',
 'Bangalore'),
('Modern Furniture',
 'modernfurniture@gmail.com',
 '9876543212',
 'Chennai');

INSERT INTO products
(product_name, category_id, supplier_id, price, stock_quantity, reorder_level)
VALUES
('Laptop', 1, 1, 55000, 15, 5),
('Keyboard', 1, 1, 1200, 25, 10),
('Mouse', 4, 1, 700, 30, 10),
('Notebook', 2, 2, 80, 50, 20),
('Office Chair', 3, 3, 7500, 8, 5),
('Monitor', 1, 1, 15000, 12, 5);