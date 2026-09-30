from utils import read_file
from products import PRODUCTS_FILE
from sales import SALES_FILE


def report_product():
    print("Report Product".center(40))
    print("=" * 40)
    print("| No. |   Product Name  |     price    |")
    print("=" * 40)
    for line in read_file(PRODUCTS_FILE):
        product_id, name, price = line.split(",")
        print(f"|{product_id:^5}| {name:^16}| {float(price):^13}|")
    print("=" * 40)


def report_sales_by_product():
    totals = {}
    for line in read_file(SALES_FILE):
        _, name, _, total = line.split(",")
        totals[name] = totals.get(name, 0) + float(total)

    print("Sales by Product".center(36))
    print("=" * 36)
    print("|  Product Name   |  Total Sales   |")
    print("=" * 36)
    for name, total in totals.items():
        print(f"|{name:^16} | {total:^9} bath |")
    print("=" * 36)


def report_total_sales():
    total = sum(float(line.split(",")[3]) for line in read_file(SALES_FILE))
    print(f"Total sales: {total} bath")
