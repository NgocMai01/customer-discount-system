def calculate_discount(total_spent_before, current_order):
    """
    Hàm tính toán SỐ TIỀN GIẢM GIÁ (VNĐ) cho đơn hàng hiện tại.
    - Trả về 10% giá trị đơn hàng hiện tại nếu tổng tích lũy đạt từ 50 triệu trở lên.
    - Trả về 0 nếu không đủ điều kiện.
    """
    # 1. Tính tổng chi tiêu tích lũy bao gồm cả đơn hàng mới
    total_spent_with_current = total_spent_before + current_order
    
    # 2. Kiểm tra điều kiện đạt từ 50 triệu đồng trở lên
    if total_spent_with_current >= 50000000:
        # Trả về số tiền giảm giá cụ thể (10% của đơn hàng hiện tại)
        return current_order * 0.1
    else:
        # Không được giảm giá
        return 0