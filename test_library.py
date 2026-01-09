from library import calculate_library_fine

def test_fine_under_5_days(capsys):
    calculate_library_fine("Alice", "Math Book", 3)
    captured = capsys.readouterr().out
    assert "Total Fine   : ₹ 6" in captured  # 3*2=6

def test_fine_between_6_and_10_days(capsys):
    calculate_library_fine("Bob", "Science Book", 7)
    captured = capsys.readouterr().out
    assert "Total Fine   : ₹ 35" in captured  # 7*5=35

def test_fine_above_10_days(capsys):
    calculate_library_fine("Charlie", "History Book", 12)
    captured = capsys.readouterr().out
    assert "Total Fine   : ₹ 120" in captured  # 12*10=120
