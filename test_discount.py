from discount import calculate_discount

def test_tc01():
    # TC01: tổng trước 60tr, đơn hàng 2tr -> kỳ vọng giảm 200.000
    result = calculate_discount(60000000, 2000000)
    assert result == 200000


def test_tc02():
    # TC02: tổng trước 30tr, đơn hàng 2tr -> kỳ vọng giảm 0
    result = calculate_discount(30000000, 2000000)
    assert result == 0


def test_tc03():
    # TC03: tổng trước 49tr, đơn hàng 2tr -> kỳ vọng giảm 200.000 (vì sau đơn hàng đạt 51tr)
    result = calculate_discount(49000000, 2000000)
    assert result == 200000