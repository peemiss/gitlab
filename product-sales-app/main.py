from products import add_product
from sales import buy_product
from report import report_product, report_sales_by_product, report_total_sales

INVALID = "YOUR ENTER ISN'T CORRECT TRY AGAIN"

ACTIONS = {"1": add_product, "2": report_product, "3": buy_product}
REPORTS = {"P": report_product, "S": report_sales_by_product, "T": report_total_sales}


def report_menu():
    while True:
        print()
        print("===== Report Menu =====")
        print("P = product")
        print("S = sales by product")
        print("T = total sales")
        print("0 = back")
        choice = input("Enter (P/S/T/0) : ").strip().upper()
        print()
        if choice == "0":
            break
        elif choice in REPORTS:
            REPORTS[choice]()
        else:
            print(INVALID)


def menu():
    while True:
        print("1. Add a new product")
        print("2. Show Product")
        print("3. Buy a product")
        print("4. Report")
        print("0. exit")

        choice = input("Enter your choice : ").strip()
        print()
        if choice == "0":
            break
        elif choice in ACTIONS:
            ACTIONS[choice]()
        elif choice == "4":
            report_menu()
        else:
            print(INVALID)
        print()


if __name__ == "__main__":
    menu()
