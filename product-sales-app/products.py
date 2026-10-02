from utils import read_file

PRODUCTS_FILE = "products.txt"


def read_products():
    return read_file(PRODUCTS_FILE)


def add_product():
    products = read_products()
    new_id = int(products[-1].split(",")[0]) + 1 if products else 1

    name = input("Enter product name: ")
    price = float(input("Enter price: "))

    with open(PRODUCTS_FILE, "a") as file:
        file.write(f"{new_id},{name},{price}\n")
    print("Product added successfully")