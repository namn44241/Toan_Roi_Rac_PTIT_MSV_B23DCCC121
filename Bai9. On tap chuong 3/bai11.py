# 11.	Viết hàm trong C/C++/Python sử dụng phương pháp sinh theo thứ tự từ điển liệt kê các tổ hợp chập k của tập n phần tử {1, 2, ...n}.
def next_combination(a, n, k):
    i = k
    # Tìm từ phải sang trái phần tử đầu tiên chưa đạt giới hạn trên
    while i > 0 and a[i] >= n - k + i:
        i -= 1

    if i > 0:  # Nếu tìm thấy
        a[i] += 1  # Tăng phần tử tại vị trí i
        # Điều chỉnh các phần tử phía sau
        for j in range(i + 1, k + 1):
            a[j] = a[j - 1] + 1
        return True
    return False  # Không còn cấu hình tiếp theo


def generate_combinations(n, k):
    # Khởi tạo cấu hình đầu tiên: 1,2,3,...,k
    a = [0] * (k + 1)  # a[0] không sử dụng
    for i in range(1, k + 1):
        a[i] = i

    # In cấu hình đầu tiên
    print(a[1:])

    # Sinh và in các cấu hình tiếp theo
    while next_combination(a, n, k):
        print(a[1:])


# Test với n = 5, k = 3
n = 5
k = 3
print(f"Các tổ hợp chập {k} của tập {{1, 2, ..., {n}}}:")
generate_combinations(n, k)