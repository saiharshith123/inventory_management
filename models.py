class Product:
    def __init__(
        self,
        product_id,
        product_name,
        category_id,
        supplier_id,
        price,
        stock_quantity,
        reorder_level
    ):
        self.product_id = product_id
        self.product_name = product_name
        self.category_id = category_id
        self.supplier_id = supplier_id
        self.price = price
        self.stock_quantity = stock_quantity
        self.reorder_level = reorder_level

    def __str__(self):
        return (
            f"{self.product_id} | "
            f"{self.product_name} | "
            f"₹{self.price} | "
            f"Stock: {self.stock_quantity}"
        )