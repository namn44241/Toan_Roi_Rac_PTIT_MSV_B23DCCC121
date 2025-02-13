def count_solutions():
    count = 0
    # Duyệt x2 trong khoảng [3,8]
    for x2 in range(3, 9):
        # Duyệt x4 trong khoảng [2,6]
        for x4 in range(2, 7):
            # Số còn lại cần phân phối cho x1, x3, x5, x6
            remaining = 30 - x2 - x4

            # Nếu số còn lại âm, bỏ qua trường hợp này
            if remaining < 0:
                continue

            # Sử dụng công thức tổ hợp lặp để đếm cách phân phối
            # remaining vào 4 biến không âm (x1, x3, x5, x6)
            # Công thức: C(n+k-1,k) với n là số biến, k là tổng cần phân phối
            n = 4  # số biến (x1, x3, x5, x6)
            k = remaining  # số cần phân phối
            result = 1

            # Tính C(n+k-1,k) = C(n+k-1,n-1)
            # C(n,k) = n!/(k!(n-k)!)
            numerator = 1  # tử số
            denominator = 1  # mẫu số

            # Tính tổ hợp C(n+k-1,n-1)
            for i in range(n - 1):
                numerator *= (k + n - 1 - i)
                denominator *= (i + 1)

            count += numerator // denominator

    return count


# Tính kết quả
result = count_solutions()
print(f"Số nghiệm thỏa mãn: {result}")