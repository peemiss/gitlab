import pytest

from utils import read_file
from products import PRODUCTS_FILE
from sales import SALES_FILE


@pytest.mark.parametrize("file_product, file_sales", [
    (PRODUCTS_FILE, "product"),
    (SALES_FILE, "sales")
])
def test_read_file(file_product, file_sales):

    result = read_file(file_product)

    assert len(result) > 0

    for line in result:

        if file_sales == "product":

            product_id, name, price = line.split(",")

            assert product_id != ""
            assert name != ""
            assert float(price) >= 0

        else:

            product_id, name, quantity, total = line.split(",")

            assert product_id != ""
            assert name != ""
            assert int(quantity) > 0
            assert float(total) >= 0


def test_read_file_not_found():

    result = read_file("not_found.txt")

    assert result == []
