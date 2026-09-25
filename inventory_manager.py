from db import get_connection

class InventoryManager:
    def add_product(
        self,
        name,
        category_id,
        supplier_id,
        price,
        stock,
        reorder_level
    ):
        connection = get_connection()
        if not connection:
            return

        try:
            cursor = connection.cursor()
            query = """
                INSERT INTO products
                (
                    product_name,
                    category_id,
                    supplier_id,
                    price,
                    stock_quantity,
                    reorder_level
                )
                VALUES (%s, %s, %s, %s, %s, %s)
                RETURNING product_id
            """
            cursor.execute(
                query,
                (
                    name,
                    category_id,
                    supplier_id,
                    price,
                    stock,
                    reorder_level
                )
            )
            product_id = cursor.fetchone()[0]
            connection.commit()
            print(
                f"\nProduct added successfully."
                f" Product ID: {product_id}"
            )

        except Exception as error:
            connection.rollback()
            print("Error:", error)

        finally:
            cursor.close()
            connection.close()

    def get_products(self):
        connection = get_connection()
        if not connection:
            return []

        try:
            cursor = connection.cursor()
            query = """
                SELECT
                    p.product_id,
                    p.product_name,
                    c.category_name,
                    s.supplier_name,
                    p.price,
                    p.stock_quantity,
                    p.reorder_level
                FROM products p
                JOIN categories c
                    ON p.category_id = c.category_id
                JOIN suppliers s
                    ON p.supplier_id = s.supplier_id
                ORDER BY p.product_id
            """
            cursor.execute(query)
            return cursor.fetchall()

        except Exception as error:
            print("Error:", error)
            return []
        
        finally:
            cursor.close()
            connection.close()

    def get_product(self, product_id):
        connection = get_connection()
        if not connection:
            return None

        try:
            cursor = connection.cursor()
            query = """
                SELECT
                    p.product_id,
                    p.product_name,
                    c.category_name,
                    s.supplier_name,
                    p.price,
                    p.stock_quantity,
                    p.reorder_level
                FROM products p
                JOIN categories c
                    ON p.category_id = c.category_id
                JOIN suppliers s
                    ON p.supplier_id = s.supplier_id
                WHERE p.product_id = %s
            """
            cursor.execute(query, (product_id,))
            return cursor.fetchone()

        finally:
            cursor.close()
            connection.close()

    def update_product(
        self,
        product_id,
        name,
        price,
        reorder_level
    ):
        connection = get_connection()
        if not connection:
            return

        try:
            cursor = connection.cursor()
            query = """
                UPDATE products
                SET
                    product_name = %s,
                    price = %s,
                    reorder_level = %s
                WHERE product_id = %s
            """
            cursor.execute(
                query,
                (
                    name,
                    price,
                    reorder_level,
                    product_id
                )
            )
            connection.commit()
            if cursor.rowcount == 0:
                print("Product not found.")
            else:
                print("Product updated successfully.")

        except Exception as error:
            connection.rollback()
            print("Error:", error)

        finally:
            cursor.close()
            connection.close()

    def delete_product(self, product_id):
        connection = get_connection()
        if not connection:
            return

        try:
            cursor = connection.cursor()
            query = """
                DELETE FROM products
                WHERE product_id = %s
            """
            cursor.execute(query, (product_id,))
            connection.commit()
            if cursor.rowcount == 0:
                print("Product not found.")
            else:
                print("Product deleted successfully.")

        except Exception as error:
            connection.rollback()
            print(
                "Cannot delete product."
                " It may have associated transactions."
            )
        finally:
            cursor.close()
            connection.close()

    def search_product(self, keyword):
        connection = get_connection()
        if not connection:
            return []

        try:
            cursor = connection.cursor()
            query = """
                SELECT
                    p.product_id,
                    p.product_name,
                    c.category_name,
                    p.price,
                    p.stock_quantity
                FROM products p
                JOIN categories c
                    ON p.category_id = c.category_id
                WHERE LOWER(p.product_name)
                    LIKE LOWER(%s)
                ORDER BY p.product_name
            """
            cursor.execute(
                query,
                (f"%{keyword}%",)
            )
            return cursor.fetchall()

        finally:
            cursor.close()
            connection.close()

    def purchase_stock(
        self,
        product_id,
        quantity,
        purchase_price
    ):
        connection = get_connection()
        if not connection:
            return

        try:
            cursor = connection.cursor()
            cursor.execute(
                """
                INSERT INTO purchases
                (
                    product_id,
                    quantity,
                    purchase_price
                )
                VALUES (%s, %s, %s)
                """,
                (
                    product_id,
                    quantity,
                    purchase_price
                )
            )
            cursor.execute(
                """
                UPDATE products

                SET stock_quantity =
                    stock_quantity + %s

                WHERE product_id = %s
                """,
                (
                    quantity,
                    product_id
                )
            )
            if cursor.rowcount == 0:
                raise Exception("Product does not exist.")
            connection.commit()
            print("Purchase recorded successfully.")
            print("Stock updated successfully.")

        except Exception as error:
            connection.rollback()
            print("Transaction failed:", error)

        finally:
            cursor.close()
            connection.close()

    def sell_product(
        self,
        product_id,
        quantity,
        sale_price
    ):
        connection = get_connection()
        if not connection:
            return

        try:
            cursor = connection.cursor()
            cursor.execute(
                """
                SELECT stock_quantity
                FROM products
                WHERE product_id = %s
                FOR UPDATE
                """,
                (product_id,)
            )
            result = cursor.fetchone()
            if not result:
                raise Exception("Product not found.")
            current_stock = result[0]
            if current_stock < quantity:
                raise Exception(
                    f"Insufficient stock."
                    f" Available: {current_stock}"
                )
            cursor.execute(
                """
                INSERT INTO sales
                (
                    product_id,
                    quantity,
                    sale_price
                )
                VALUES (%s, %s, %s)
                """,
                (
                    product_id,
                    quantity,
                    sale_price
                )
            )
            cursor.execute(
                """
                UPDATE products
                SET stock_quantity =
                    stock_quantity - %s
                WHERE product_id = %s
                """,
                (
                    quantity,
                    product_id
                )
            )
            connection.commit()
            print("Sale recorded successfully.")
            print("Stock updated successfully.")

        except Exception as error:
            connection.rollback()
            print("Sale failed.")
            print("Transaction rolled back.")
            print(error)

        finally:
            cursor.close()
            connection.close()