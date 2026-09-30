from products import read_products

SALES_FILE = "sales.txt"


def buy_product():
    product_id = input("Enter product id: ")
    quantity = int(input("Enter quantity: "))

    product = next((p for p in read_products() if p.split(",")[0] == product_id), None)
    if product is None:
        print("Product not found")
        return None

    _, name, price = product.split(",")
    total_price = float(price) * quantity

    with open(SALES_FILE, "a") as file:
        file.write(f"{product_id},{name},{quantity},{total_price}\n")
    print(f"Sold {quantity} {name} for {total_price} bath")
    return product_id, name, quantity, total_price
