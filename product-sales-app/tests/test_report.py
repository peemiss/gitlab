from report import report_product
def test_report_product(capsys):
    report_product()
    captured = capsys.readouterr()
    assert "|1 | pepsi | 15.0 |" in captured.out
    assert "|2 | oishi | 25.0 |" in captured.out
    assert "|3 | Ley | 20.0 |" in captured.out
    assert "|4 | water | 10.0" in captured.out
    assert "|5 | Tomyum | 50.0" in captured.out