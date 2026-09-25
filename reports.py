from db import get_connection

class Reports:
    def inventory_report(self):
        connection = get_connection()
        if not connection:
            return

        try:
            cursor = connection.cursor()
            query = """
                SELECT
                    p.product_name,
                    c.category_name,
                    s.supplier_name,
                    p.price,
                    p.stock_quantity,
                    p.reorder_level,
                    CASE
                        WHEN p.stock_quantity <= p.reorder_level
                        THEN 'REORDER'
                        ELSE 'OK'
                    END AS stock_status
                FROM products p
                JOIN categories c
                    ON p.category_id = c.category_id
                JOIN suppliers s
                    ON p.supplier_id = s.supplier_id
                ORDER BY p.stock_quantity ASC
            """
            cursor.execute(query)
            rows = cursor.fetchall()
            print("\n========== INVENTORY REPORT ==========\n")

            if not rows:
                print("No inventory records found.")
                return

            for row in rows:
                print(f"Product       : {row[0]}")
                print(f"Category      : {row[1]}")
                print(f"Supplier      : {row[2]}")
                print(f"Price         : ₹{row[3]}")
                print(f"Stock         : {row[4]}")
                print(f"Reorder Level : {row[5]}")
                print(f"Status        : {row[6]}")
                print("-" * 40)

        except Exception as error:
            print("Error generating inventory report:")
            print(error)

        finally:
            cursor.close()
            connection.close()

    def sales_report(self):
        connection = get_connection()
        if not connection:
            return

        try:
            cursor = connection.cursor()
            query = """
                SELECT
                    p.product_name,
                    SUM(s.quantity) AS total_quantity,
                    SUM(
                        s.quantity * s.sale_price
                    ) AS revenue
                FROM sales s
                JOIN products p
                    ON s.product_id = p.product_id
                GROUP BY
                    p.product_id,
                    p.product_name

                ORDER BY revenue DESC
            """
            cursor.execute(query)
            rows = cursor.fetchall()
            print("\n========== SALES REPORT ==========\n")

            if not rows:
                print("No sales records found.")
                return

            for row in rows:
                print(f"Product       : {row[0]}")
                print(f"Quantity Sold : {row[1]}")
                print(f"Revenue       : ₹{row[2]}")
                print("-" * 40)

        except Exception as error:
            print("Error generating sales report:")
            print(error)

        finally:
            cursor.close()
            connection.close()

    def category_report(self):
        connection = get_connection()
        if not connection:
            return

        try:
            cursor = connection.cursor()
            query = """
                SELECT
                    c.category_name,
                    COUNT(p.product_id)
                        AS total_products,
                    COALESCE(
                        SUM(p.stock_quantity),
                        0
                    ) AS total_stock,
                    COALESCE(
                        SUM(
                            p.stock_quantity * p.price
                        ),
                        0
                    ) AS inventory_value
                FROM categories c
                LEFT JOIN products p
                    ON c.category_id = p.category_id
                GROUP BY
                    c.category_id,
                    c.category_name
                ORDER BY inventory_value DESC
            """
            cursor.execute(query)
            rows = cursor.fetchall()
            print("\n========== CATEGORY REPORT ==========\n")
            if not rows:
                print("No category records found.")
                return

            for row in rows:
                print(f"Category        : {row[0]}")
                print(f"Products        : {row[1]}")
                print(f"Total Stock     : {row[2]}")
                print(f"Inventory Value : ₹{row[3]}")
                print("-" * 40)

        except Exception as error:
            print("Error generating category report:")
            print(error)

        finally:
            cursor.close()
            connection.close()

    def dashboard(self):
        connection = get_connection()
        if not connection:
            return

        try:
            cursor = connection.cursor()
            query = """
                SELECT
                    COUNT(*) AS products,
                    COALESCE(
                        SUM(stock_quantity),
                        0
                    ) AS total_stock,
                    COALESCE(
                        SUM(
                            stock_quantity * price
                        ),
                        0
                    ) AS inventory_value,
                    COALESCE(
                        (
                            SELECT
                                SUM(
                                    quantity * sale_price
                                )
                            FROM sales
                        ),
                        0
                    ) AS total_revenue
                FROM products
            """
            cursor.execute(query)
            result = cursor.fetchone()
            print("\n")
            print("=" * 50)
            print("          INVENTORY DASHBOARD")
            print("=" * 50)

            print(
                f"Total Products      : {result[0]}"
            )
            print(
                f"Total Stock         : {result[1]}"
            )
            print(
                f"Inventory Value     : ₹{result[2]}"
            )
            print(
                f"Total Sales Revenue : ₹{result[3]}"
            )
            print("=" * 50)

        except Exception as error:
            print("Error generating dashboard:")
            print(error)

        finally:
            cursor.close()
            connection.close()