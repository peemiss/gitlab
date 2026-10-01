import pytest

from sales import buy_product
from utils import read_file
from products import PRODUCTS_FILE


@pytest.fixture
def products_data():
    return read_file(PRODUCTS_FILE)

@pytest.mark.parametrize("input_data", [
    ["3", "1"],
    ["3", "2"],
    ["3", "5"]
])
def test_buy_product(capsys, monkeypatch, tmp_path, products_data, input_data):

    product_id, name, price = products_data[2].split(",")

    inputs = iter(input_data)

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs)
    )

    sales_file = tmp_path / "sales.txt"
    monkeypatch.setattr("sales.SALES_FILE", str(sales_file))

    result = buy_product()
    captured = capsys.readouterr()

    quantity = int(input_data[1])

    assert result[0] == product_id
    assert result[1] == name
    assert result[2] == quantity
    assert result[3] == pytest.approx(float(price) * quantity)

    assert f"Sold {quantity} {name}" in captured.out


def test_buy_product_error(capsys, monkeypatch):

    inputs = iter(["10", "2"])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs)
    )

    result = buy_product()
    captured = capsys.readouterr()

    assert result is None
    assert "Product not found" in captured.out