from inventory_manager import InventoryManager
from reports import Reports

inventory = InventoryManager()
reports = Reports()

def display_products(products):
    if not products:
        print("\nNo products found.")
        return
    print("\n" + "=" * 90)
    print(
        f"{'ID':<5}"
        f"{'Product':<20}"
        f"{'Category':<15}"
        f"{'Supplier':<20}"
        f"{'Price':<12}"
        f"{'Stock':<8}"
        f"{'Reorder':<8}"
    )
    print("=" * 90)
    for product in products:
        print(
            f"{product[0]:<5}"
            f"{product[1]:<20}"
            f"{product[2]:<15}"
            f"{product[3]:<20}"
            f"{product[4]:<12}"
            f"{product[5]:<8}"
            f"{product[6]:<8}"
        )

def add_product():
    print("\n========== ADD PRODUCT ==========")
    name = input("Product name: ")
    category_id = int(
        input("Category ID: ")
    )
    supplier_id = int(
        input("Supplier ID: ")
    )
    price = float(
        input("Price: ")
    )
    stock = int(
        input("Initial stock: ")
    )
    reorder = int(
        input("Reorder level: ")
    )
    inventory.add_product(
        name,
        category_id,
        supplier_id,
        price,
        stock,
        reorder
    )

def update_product():
    print("\n========== UPDATE PRODUCT ==========")
    product_id = int(
        input("Product ID: ")
    )
    name = input(
        "New product name: "
    )
    price = float(
        input("New price: ")
    )
    reorder = int(
        input("New reorder level: ")
    )
    inventory.update_product(
        product_id,
        name,
        price,
        reorder
    )

def delete_product():
    print("\n========== DELETE PRODUCT ==========")
    product_id = int(
        input("Product ID: ")
    )
    confirm = input(
        "Are you sure? (y/n): "
    )
    if confirm.lower() == "y":
        inventory.delete_product(
            product_id
        )

def search_product():
    keyword = input(
        "\nEnter product name to search: "
    )
    products = inventory.search_product(
        keyword
    )

    print("\n========== SEARCH RESULTS ==========")
    for product in products:
        print(
            f"ID: {product[0]} | "
            f"{product[1]} | "
            f"Category: {product[2]} | "
            f"Price: ₹{product[3]} | "
            f"Stock: {product[4]}"
        )

def purchase_stock():
    print("\n========== PURCHASE STOCK ==========")
    product_id = int(
        input("Product ID: ")
    )
    quantity = int(
        input("Quantity purchased: ")
    )
    price = float(
        input("Purchase price: ")
    )
    inventory.purchase_stock(
        product_id,
        quantity,
        price
    )

def sell_product():
    print("\n========== SELL PRODUCT ==========")
    product_id = int(
        input("Product ID: ")
    )
    quantity = int(
        input("Quantity sold: ")
    )
    price = float(
        input("Selling price: ")
    )
    inventory.sell_product(
        product_id,
        quantity,
        price
    )

def menu():
    while True:
        print("\n")
        print("=" * 50)
        print("     INVENTORY MANAGEMENT SYSTEM")
        print("=" * 50)

        print("1. Dashboard")
        print("2. View Products")
        print("3. Add Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Search Product")
        print("7. Purchase Stock")
        print("8. Sell Product")
        print("9. Inventory Report")
        print("10. Sales Report")
        print("11. Category Report")
        print("0. Exit")

        print("=" * 50)

        choice = input(
            "Enter your choice: "
        )

        try:
            if choice == "1":
                reports.dashboard()

            elif choice == "2":
                products = inventory.get_products()
                display_products(products)

            elif choice == "3":
                add_product()

            elif choice == "4":
                update_product()

            elif choice == "5":
                delete_product()

            elif choice == "6":
                search_product()

            elif choice == "7":
                purchase_stock()

            elif choice == "8":
                sell_product()

            elif choice == "9":
                reports.inventory_report()

            elif choice == "10":
                reports.sales_report()

            elif choice == "11":
                reports.category_report()

            elif choice == "0":
                print(
                    "\nThank you for using "
                    "Inventory Management System!"
                )
                break

            else:
                print(
                    "\nInvalid choice."
                )

        except ValueError:
            print(
                "\nPlease enter valid values."
            )

        except Exception as error:
            print(
                f"\nUnexpected error: {error}"
            )

if __name__ == "__main__":
    menu()