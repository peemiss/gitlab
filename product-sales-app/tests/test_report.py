import pytest

from report import (report_product,report_sales_by_product,report_total_sales)

from utils import read_file
from products import PRODUCTS_FILE
from sales import SALES_FILE

@pytest.fixture
def products_data():
    return read_file(PRODUCTS_FILE)

@pytest.fixture
def sales_data():
    return read_file(SALES_FILE)

def test_report_product(capsys, products_data):

    report_product()

    captured = capsys.readouterr()

    assert "Report Product" in captured.out
    assert "Product Name" in captured.out
    assert "price" in captured.out

    assert len(products_data) > 0

    for line in products_data:

        product_id = line.split(",")[0]
        name = line.split(",")[1] 
        price = float(line.split(",")[2])
        
        assert product_id != ""
        assert name != ""
        assert price >= 0

        assert name in captured.out
        assert str(price) in captured.out

def test_report_sales_by_product(capsys, sales_data):

    report_sales_by_product()

    captured = capsys.readouterr()

    assert "Sales by Product" in captured.out
    assert "Product Name" in captured.out
    assert "Total Sales" in captured.out

    assert len(sales_data) > 0

    for line in sales_data:

        product_id = line.split(",")[0]
        name = line.split(",")[1]
        quantity = int(line.split(",")[2])
        total = float(line.split(",")[3])

        assert product_id != ""
        assert name != ""
        assert quantity > 0
        assert total >= 0

        assert name in captured.out
        assert str(total) in captured.out

def test_report_total_sales(capsys, sales_data):

    report_total_sales()

    captured = capsys.readouterr()

    total = sum(
        float(line.split(",")[3])
        for line in sales_data
    )
    
    assert total == pytest.approx(390.0)

    assert "Total sales:" in captured.out

    assert f"{total}" in captured.out