def calculate_binary_strings(n):
    # Khởi tạo các giá trị ban đầu
    if n < 1:
        return 0

    # a1 = 2 (0,1)
    # a2 = 3 (00,01,10)
    # a3 = 4 (000,001,010,100)
    a = [0] * (n + 1)
    a[1] = 2
    a[2] = 3
    a[3] = 4

    # Tính các giá trị tiếp theo theo công thức hồi quy
    for i in range(4, n + 1):
        a[i] = a[i - 1] + a[i - 2] + a[i - 3]

    return a[n]


# Tính a7
n = 7
result = calculate_binary_strings(n)
print(f"Số xâu nhị phân độ dài {n} không chứa ba số 1 liên tiếp là: {result}")

# In ra các giá trị từ a1 đến a7 để kiểm tra
for i in range(1, n + 1):
    print(f"a{i} = {calculate_binary_strings(i)}")