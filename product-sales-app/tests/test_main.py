import main


def test_menu(monkeypatch, capsys):
    #จำลองให้ผู้ใช้เลือก 0 ทันที
    monkeypatch.setattr("builtins.input", lambda _: "0")

    main.menu()

    #เมนูต้องแสดงครบทุกข้อ
    out = capsys.readouterr().out
    for text in ("1. Add a new product", "2. Show Product",
                 "3. Buy a product", "4. Report", "0. exit"):
        assert text in out


def test_report_menu(tmp_path, monkeypatch, capsys):
    #จำลองให้เลือก T แล้วกลับ (0)
    monkeypatch.chdir(tmp_path)
    answers = iter(["t", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(answers))

    main.report_menu()

    #เลือก T ต้องแสดงยอดขายรวม (ยังไม่มียอดขายจึงเป็น 0)
    assert "Total sales: 0 bath" in capsys.readouterr().out