from products import read_products, add_product


def test_read_products(tmp_path, monkeypatch):
    #สร้างโฟลเดอร์ชั่วคราว แล้วย้ายไปทำงานที่นั่น
    (tmp_path / "products.txt").write_text("1,Ley,22.0\n2,Pepsi,25.0\n")
    monkeypatch.chdir(tmp_path)

    assert read_products() == ["1,Ley,22.0", "2,Pepsi,25.0"]


def test_add_product(tmp_path, monkeypatch, capsys):
    # สร้าง id ใหม่จำลองการพิมพ์ชื่อ/ราคา 
    (tmp_path / "products.txt").write_text("1,Ley,22.0\n")
    monkeypatch.chdir(tmp_path)
    answers = iter(["Water", "10"])
    monkeypatch.setattr("builtins.input", lambda _: next(answers))

    add_product()

    #id ต่อจากเดิมเป็น 2 และมีข้อความแจ้งสำเร็จ
    assert read_products() == ["1,Ley,22.0", "2,Water,10.0"]
    assert "Product added successfully" in capsys.readouterr().out