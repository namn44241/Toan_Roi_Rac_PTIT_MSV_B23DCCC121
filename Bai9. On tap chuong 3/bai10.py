# 10.	Viết hàm trong C/C++/Python sử dụng phương pháp quay lui liệt kê các xâu nhị phân độ dài n.
# Sau đó trình bày cây biểu diễn quá trình hoạt động của hàm khi sinh các xâu nhị phân độ dài 3.
def print_binary(arr, n):
    # In xâu nhị phân hiện tại
    for i in range(n):
        print(arr[i], end='')
    print()

def try_binary(i, n, arr):
    # Thử các giá trị 0, 1 cho vị trí i
    for j in range(2):  # j chạy từ 0 đến 1
        arr[i] = j
        if i == n - 1:  # Nếu đã đủ n phần tử
            print_binary(arr, n)
        else:
            try_binary(i + 1, n, arr)  # Quay lui cho vị trí tiếp theo

def generate_binary(n):
    arr = [0] * n  # Khởi tạo mảng n phần tử
    try_binary(0, n, arr)

# Test với n = 3
n = 3
print(f"Các xâu nhị phân độ dài {n}:")
generate_binary(n)